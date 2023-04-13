'''
lista é uma estrutura de dados. variavel que consegue
guardar vários tipos de variáveis nela.

'''

#Antes
nota1 = 7.9
nota2 = 9.7
nota3 = 8.2

#Com lista
notas = [7.9, 9.7, 8.2]

#Criando listas (listas permitem numeros reais, decimais, str)
lista = [] #lista vazia que se pode adicionar valores com o tempo
lista = list() #outro modelo de lista vazia
lista = [26, 'Simara', 3.14159, True] #não retorna erro
lista_de_listas = [10, [1, 2, 3]]     #um elemento é um numero inteiro e adicionar outra lista

#Indexação e Slices (indexação: forma que se acessa um elemento da lista por meio de um índice)

lista = [26, 'Simara', 3.14159, True]

print(lista[0]) #índices sempre começam do zero
print(lista[1])
print(lista[2])
print(lista[3])
print(lista[-1]) #acessa o último índice 

#(slices: acessa um pedaço da lista)

lista = [10, 50, 30, 40, 25, 60, 5]
print(lista[0:3]) #começa no índice 0 e vai atémenor do que o 3
print(lista[3:6])
print(lista[3:0])
print(lista[2:6:2]) #pula de 2 em 2 e vai até o 6º numero

#Utilizando os próprios elementos da lista
#percorre cada elemento dentro da lista
for elemento in lista:
    print(elemento)

#para saber quantos elementos tem dentro da lista

print("Comprimento da lista: ", len(lista))

for i in range(len(lista)):
    print(i)


for i in range(len(lista)): #neste imprime cada elemento da lista pelo índice
    print(lista[i])
