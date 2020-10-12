PS C:\GitHub\pythonbirds> python
Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:43:08) [MSC v.1926 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license" for more information.

>>> nome = 'Eduardo'
>>> nome
'Eduardo'

>>> nome.upper() // upper() - Maisculo
'EDUARDO'

>>> nome.lower() // lower() - Minusculo
'eduardo'

>>> nome[0]
'E'

>>> nome[1]
'd'

>>> nome[2]
'u'

>>> len(nome)  // len - tamanho da string nome
7   

// Para pegar o ultimo elemento da string nome
>>> tamanho = len(nome)
>>> tamanho
7   

>>> nome[tamanho - 1] 	// Para pegar o ultimo elemento da string nome
'o' 

>>> nome[len(nome) - 1]  // Outra forma de pegar o ultimo elemento da string nome
'o'

>>> nome[-1]  // Para pegar o ultimo elemento da string nome
'o'

>>> nome[-2]  // Para pegar o penultimo elemento da string nome
'd'

>>> nome[0:3] // Para pegar da posição 0  até(:) 3 elemento da string nome  // 'Edu'
'Edu'

>>> nome[0:5] 				// os intervalos são fechados no inicio e abertos no final
'Eduar'

>>> nome[0:7]
'Eduardo'

>>> nomeCompleto = 'Eduardo da Silva Rodrigues'
>>> nomeCompleto
'Eduardo da Silva Rodrigues'

>>> nomeCompleto[len(nomeCompleto) -1]   // Para pegar o ultimo elemento da str
's'

>>> nomeCompleto[0:7]
'Eduardo'

>>> len(nomeCompleto)		// Tamanho da str
26

>>> nomeCompleto[8:26]
'da Silva Rodrigues'

>>> nomeCompleto[:]			// Criar uma cópia da str inteira
'Eduardo da Silva Rodrigues'

>>> nomeCompleto[0:7:2]		// Pegar todos os caracteres pares até posição 7
'Euro'

>>> nomeCompleto[::2]   	// Pegar todos os caracteres pares da str inteira
'Eurod iv orge'

>>> nome[::-1]				// Str nome imprimir ao contrario, ou seja, imprimir a str de traz p/ frente
'odraudE'

>>> nomeCompleto[::-1]		// Imprimir o nome ao contrario
'seugirdoR avliS ad odraudE'

// A lista em Python pode incluir qualquer objeto. Vamos criar uma lista de Interios

>>> inteiros = [0,1,2,3]	// Criar uma lista
>>> inteiros
[0, 1, 2, 3]
>>> type(inteiros)
<class 'list'>

>>> len(inteiros)
4
>>> inteiros[0]
0
>>> inteiros[1]
1
>>> inteiros[2]
2
>>> inteiros[3]
3
>>> inteiros[4]				// Na lista de inteiros não temos a 4º posição da lista, pois a lista de inteiros começa na posição 0(zero)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list index out of range
>>> 

>>> inteiros[::-1]		// Imprimir a lista ao contrario, ou seja, imprimir a lista de inteiros de traz p/ frente
[3, 2, 1, 0]

>>> dias=['Seg', 'Ter', 'Qua', 'Qui', 'Sex']	// Lista de dias da semana
>>> dias
['Seg', 'Ter', 'Qua', 'Qui', 'Sex']

>>> dias[0] 			// Primeiro elemento da lista
'Seg'

>>> dias[-1]			// Ultimo elemento da lista
'Sex'

>>> dias[::-1]			// Imprime a lista de dias invertida
['Sex', 'Qui', 'Qua', 'Ter', 'Seg']

>>> separadorPalavras = nomeCompleto.split()		// split() - Médodo da str para separar os itens da lista
>>> separadorPalavras
['Eduardo', 'da', 'Silva', 'Rodrigues']

>>>
>>> nomeCompleto
'Eduardo da Silva Rodrigues'

>>> nome, sobrenome = separadorPalavras[0], separadorPalavras[-1]	// Separar o Nome e Sobrenome
>>> nome
'Eduardo'
>>> sobrenome
'Rodrigues'

>>>
>>> nome[0:3]
'Edu'
>>> sobrenome[0:3]
'Rod'

>>>
>>> separadorPalavras
['Eduardo', 'da', 'Silva', 'Rodrigues']

>>> '-'.join(separadorPalavras)					// join() - criar um separador nas palavras da lista
'Eduardo-da-Silva-Rodrigues'
>>> nome_hifen=_    							//  nome_hifen é atribuido o resultado da str da linha acima
>>> nome_hifen  
'Eduardo-da-Silva-Rodrigues'

>>> nome_hifen.split()							// split() - Médodo da str para separar os itens da lista
['Eduardo-da-Silva-Rodrigues']

>>> nome_hifen.split('-')						// split('-') - Separa os itens da lista da str e retira o hifen da str
['Eduardo', 'da', 'Silva', 'Rodrigues']

>>> lista = list(range(10))						// Criar uma lista de 10 posições de numeros, 0 até 9
>>> lista
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

>>> lista = list(range(20)) 					/ Criar uma lista de 20 posições de numeros, 0 até 19
>>> lista
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

>>>
>>> lista1 = list(range(6))					// [0, 1, 2, 3, 4, 5]
>>> lista2 = list(range(6,10))				// [6, 7, 8, 9]
>>> lista1 + lista2							// [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

>>> lista1
[0, 1, 2, 3, 4, 5]
>>> lista2
[6, 7, 8, 9]
>>> lista1 + lista2
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>>
>>> nome='Eduardo'
>>> sobrenome='Rodrigues'
>>> nome + sobrenome						// Exemplo de concatenação de str
'EduardoRodrigues'
>>>
>>> 'Lorem Ipsum! ' * 3
'Lorem Ipsum! Lorem Ipsum! Lorem Ipsum! '

// Tupla								// Tupla é diferente de Lista. Na tupla, não consigo alterar a Tupla (adicionar e remover elementos da Tupla)
										// Tupla é utilizado na prática quando precisa que conteiner de elementos não seja alterado. 
										// Exemplos de Tuplas : Coordenadas Geograficas, meses do anos e dias da semana.
>>> t = (1, 2, 3)
>>> len(t)
3   
>>> t[0]
1   
>>> t[0:2]
(1, 2)

// Lista
>>> lista = [0, 1, 2, 3, 4]
>>> lista
[0, 1, 2, 3, 4]
>>> lista.append(5)						// append() - Adiciona elementos na lista
>>> lista
[0, 1, 2, 3, 4, 5]
>>> lista.append(-7)
>>> lista
[0, 1, 2, 3, 4, 5, -7]

>>> lista.pop()						// pop() - Remove o ultimo elemento da lista. Retorna o valor excluido da lista.	
-7

// Lista							// Lista - eu consigo alterar os elementos da Lista, a lista é diferente da Tupla (não consigo alterar os elementos)
>>> lista
[0, 1, 2, 3, 4, 5]

>>> lista.pop(0)					// pop(0) - Remove o primeiro elemento da lista
0
>>> lista
[1, 2, 3, 4, 5]

>>> lista.insert(0, 0)				// insert(0, 0) - Insere elemento na lista na posição 0(zero) o elemento 0(zero), insert(posição da lista, valor)
>>> lista
[0, 1, 2, 3, 4, 5]
>>>

>>> t1=(1,2) + (3,4)				// Exemplo de Tuplas // No exemplo temos duas tuplas (t1 e t2), embora t1 e t2 tenham os mesmos elementos, elas são diferentes
>>> t2=(1,2) + (3,4)  
>>> t1
(1, 2, 3, 4)
>>> t2
(1, 2, 3, 4)

>>> id(t1)						// id(t1) = 11600352, ou seja, t1 e t2 são diferentes
11600352
>>> id(t2)						// id(t2) = 11600392, ou seja, t1 e t2 são diferentes
11600392
>>> t1 is t2					// t1 e t2 são iguais?
False							// Retorna Falso
>>>

// Imprimir os primeiros caracteres do meu nome
>>> nome = 'Eduardo Rodrigues'
>>> palavras = nome.split()					// Tenho que separar as palavras do meu nome
>>> palavras
['Eduardo', 'Rodrigues']
>>> print(palavras[0][0], palavras[1][0])	// Impressão que retorna os primeiros caracteres do meu nome
E R
>>>

// Exemplo do comando FOR
>>>
>>> for x in range(0,11):                 
...     print(x) 
... 
0
1
2
3
4
5
6
7
8
9
10
>>> 

// Exemplo do comando FOR 					// Impressão que retorna os primeiros caracteres do meu nome
>>> nome
'Eduardo Rodrigues'
>>> palavras = nome.split()
>>> palavras
['Eduardo', 'Rodrigues']
>>> for p in palavras:
...     print(p[0])
... 
E
R
>>>

>>> palavras='Eduardo da Silva Rodrigues'.split()		// Impressão que retorna os primeiros caracteres do meu nome
>>> palavras
['Eduardo', 'da', 'Silva', 'Rodrigues']
>>> for p in palavras:
...     print(p[0])
... 
E
d
S
R
>>>

// Imprimir somente as primeiras letras em maisculo do meu nome

>>> for p in palavras:                
...     primeiraLetra = p[0]          
...     if primeiraLetra.isupper():   
...             print(primeiraLetra)
... 
E
S
R
>>>

// Dicionário de dados em Python

>>> linguas = {'en': 'Ingles', 'pt-br': 'Portugues Brasileiro'}
>>> type(linguas)
<class 'dict'>

>>> linguas[0]									// Apresenta Error, pois o dict (dicionário de dados) não é atribuido indice de elementos conforme a Lista
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 0

>>> linguas['en']
'Ingles'
>>> linguas['pt-br']     
'Portugues Brasileiro'
>>>
>>> linguas['es'] = 'Espanhol'					// Adicionar uma nova lingua no dict, linguas['es'] = 'Espanhol'	
>>> linguas
{'en': 'Ingles', 'pt-br': 'Portugues Brasileiro', 'es': 'Espanhol'}
>>>

>>> for item in linguas:
...     print(item)
... 
en
pt-br
es

>>> for item in linguas.items():
...     print(item)
... 
('en', 'Ingles')
('pt-br', 'Portugues Brasileiro')
('es', 'Espanhol')

>>> for item in linguas.items():
...     print(item[0], item[1])
... 
en Ingles
pt-br Portugues Brasileiro
es Espanhol
>>>

>>> for chave, valor in linguas.items():
...     print(chave, valor)
... 
en Ingles
pt-br Portugues Brasileiro
es Espanhol
>>> 

// Listas - Como adicionar elementos de Lista_2 para Lista.

>>> lista=list(range(5))  
>>> lista
[0, 1, 2, 3, 4]

>>> lista_2=list(range(8,10))
>>> lista_2
[8, 9]

>>> lista.extend(lista_2)       // extend() - Função que adiciona elementos, neste caso da lista_2 para a lista (adiciona os elementos da lista). A lista_2 não é alterada.
>>> lista
[0, 1, 2, 3, 4, 8, 9]

>>> lista_2
[8, 9]
>>> lista 
[0, 1, 2, 3, 4, 8, 9]
>>>


