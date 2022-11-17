from ply.lex import lex

# carregando a lista de tokens criada no analisador lexico
from definicao_tokens import lexer

lexer.input('''
            begin
            a := 5;
            b := 8;
            c := a + b;

            write(c);

            end
            ''')
while True:
    tok = lexer.token()
    if not tok:
        break
    print(tok)
