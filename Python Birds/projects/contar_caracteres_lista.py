def contar_char(s):

    """Essa função calcula a soma de duas parcelas
    Ex:
    >>> conta_char('amor')
    a: 1
    m: 1
    o: 1
    r: 1
    >>> conta_char('amar')
    a: 2
    m: 1
    r: 1
     """

    char_ordenado = sorted(s)

    char_anterior = char_ordenado[0]

    contagem = 1

    for char_atual in char_ordenado[1:]:
        if char_atual == char_anterior:
            contagem += 1
        else:
            print(f'{char_anterior}: {contagem}')
            char_anterior = char_atual
            contagem = 1
    print(f'{char_anterior}: {contagem}')

if __name__ == '__main__':
    contar_char('amor')
    print()
    contar_char('amar')
