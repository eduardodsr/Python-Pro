'''Contagem de Caracteres com Dicionário'''

def contar_char(s):

    """Essa função calcula a quantidade de char(caracteres) de uma dict(dicionário)
    Ex:
    >>> conta_char('amor')
    {'a': 1 , 'm': 1, 'o': 1, 'r': 1}
    
    >>> conta_char('amar')
    {'a': 2, 'm': 1, 'r': 1}
     """

    resultado={} # resultado recebe um dicionário vazio

    for char in s:
        contagem = resultado.get(char, 0)
        contagem += 1
        resultado[char] = contagem
    return resultado

if __name__ == '__main__':
    print(contar_char('amor'))
    print()
    print(contar_char('amar'))
