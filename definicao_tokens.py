from ply.lex import lex

tokens = ['MAIS', 'MENOS', 'VEZES', 'DIVIDE', 'LPARENTESE',
          'RPARENTESE', 'FINAL_LINHA', 'ATRIBUICAO',
          'IGNORA_NOVA_LINHA', 'FLOAT', 'INT', 'NOME']

reserved = {
    'begin': 'BEGIN',
    'end': 'END',
    'int': 'INTEIRO',
    'float': 'DECIMAL',
    'write': 'WRITE',
    'read': 'READ'
}


tokens = tokens + list(reserved.values())

# ignora caracter em branco
t_ignore = ' \t'

t_MAIS = r'\+'
t_MENOS = r'\-'
t_VEZES = r'\*'
t_DIVIDE =r'\/'
t_LPARENTESE = r'\('
t_RPARENTESE = r'\)'
t_FINAL_LINHA = r'\;'
t_ATRIBUICAO = '\:\='


def t_IGNORA_NOVA_LINHA(t):
    r'\n'
    t.lexer.lineno += 1
    return t
    

def t_error(t):
    print(f'Caracter Ilegal {t.value[0]!r}')
    t.lexer.skip(1)

def t_FLOAT(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t


def t_INT(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_NOME(t):
     r'[a-zA-Z_][a-zA-Z_0-9]*'
     t.type = reserved.get(t.value,'NOME')   
     return t

lexer = lex()