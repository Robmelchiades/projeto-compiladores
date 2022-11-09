# projeto-compiladores


## Etapa 1

- Palavras-chave de início e fim de programa

    ```
    begin

    ...
    ...

    end
    ```
- Cabeçalho para declaração de variáveis
    ```
    <type> <var name>
    type: int, float
    ```
- Comando escrita:
    ```
    write(<var name>)
    ```
- Comando Leitura:

    ```
    read(<var name>)
    ```
- Operações de adição e subtração
    - Adição:
        ```
        <var name | num> + <var name | num>
        ```
    - Subtração:
        ```
        <var name | num> - <var name | num>
        ```
- Atribuição com um ou dois operandos (a=b+c)
    ```
    <var name> := <var name | num> + <var name | num>
    ```
- Símbolo de pontuação ao final de cada comando
    ```
    ;
    ```