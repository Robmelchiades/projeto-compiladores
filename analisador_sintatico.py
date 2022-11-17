# -----------------------------------------------------------------------------
# analisador_sintatico.py
#
# Example of using PLY To parse the following simple grammar.
#   
#   expressaoTop : BEGIN expressaoTop
#                | expressao expressaoTop
#                | END IGNORA_NOVA_LINHA
# 
#
#   expressao  : termo ATRIBUICAO
#              | termo MAIS termo
#              | termo MENOS termo
#              | termo
#              | WRITE termo
#              | READ termo
#              | INTEIRO termo
#              | DECIMAL termo
#
#   termo      : fator VEZES fator
#              | fator DIVIDE fator
#              | fator
#
#   fator      : INT
#              | NOME
#              | IGNORA_NOVA_LINHA
#              | FINAL_LINHA
#              | MAIS fator
#              | MENOS fator
#              | LPARENTESE expressao RPARENTESE
#
# -----------------------------------------------------------------------------

import ply.yacc as yacc

# carregando a lista de tokens criada no analisador lexico
from definicao_tokens import tokens

def p_expressaoTop_begin(p):
    '''
    expressaoTop  : BEGIN expressaoTop
    '''
    p[0] = ('begin', p[1], p[2])
    
def p_expressaoTop_expressao(p):
    '''
    expressaoTop  : expressao expressaoTop
    '''
    p[0] = ('expressaoTop_expressao', p[1], p[2])
    
def p_expressaoTop_end(p):
    '''
    expressaoTop  : END IGNORA_NOVA_LINHA
    '''
    p[0] = ('final_programa', p[1], p[2])

def p_expressao(p):
    '''
    expressao  : termo MAIS termo
               | termo MENOS termo
    '''
    p[0] = ('soma_subtrai', p[2], p[1], p[3])

def p_expressao_atribuicao(p):
    '''
    expressao  : termo ATRIBUICAO
    '''
    p[0] = ('atribuicao', p[1], p[2])

def p_expressao_termo(p):
    '''
    expressao : termo
    '''
    p[0] = p[1] 

def p_termo(p):
    '''
    termo   : fator VEZES fator
            | fator DIVIDE fator
    '''
    p[0] = ('multiplica_divide', p[2], p[1], p[3])
    
def p_termo_fator(p):
    '''
    termo : fator
    '''
    p[0] = p[1]

def p_fator_int(p):
    '''
    fator : INT
    '''
    p[0] = ('inteiro', p[1])

def p_fator_nome(p):
    '''
    fator : NOME
    '''
    p[0] = ('nome', p[1])

def p_fator_final_linha(p):
    '''
    fator : FINAL_LINHA
    '''
    p[0] = ('final_linha', p[1])
    
    
def p_fator_ignora_nova_linha(p):
    '''
    fator : IGNORA_NOVA_LINHA
    '''
    p[0] = ('ignora_nova_linha', p[1])


# Error rule for syntax errors
def p_error(p):
    print(p)
    print("Syntax error in input!")


# Build the parser
parser = yacc.yacc()


result = parser.parse('''
                        begin
                        a := 3 + 5;
                        end
                        ''')

print(result)
