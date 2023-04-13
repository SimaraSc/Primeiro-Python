#Métodos de lista

lista = [1, 3, 12, 8, 2]

#append (add um elemento no final dela)

print(lista)

lista.append(3) #é como se fosse uma função que está dentro de uma variável
#qr dzr que quero adicionar o 3 no final da lista

print("Depois do append: ", lista)

#insert (tbm add o elemento, mas vc escolhe a posição)

lista.insert(2, 10)
print("Depois do insert: ", lista)

#extend (junta duas listas)

lista2 = [1, 2, 3]
lista.extend(lista2)
print("Depois do extend: ", lista)

#pop (remove elemento que vc especifica a posição, se não especifica ele tira o ultimo elemento)

lista.pop()
print("Lista após o pop: ", lista)

lista.pop(0) #se especifica o valor (índice, posição), ele remove de acordo
print("Lista após o pop: ", lista)

#remove (vc especifica o valor (o elemento) que quer remover)
#e elimina o primeiro elemento indicado presente. Caso tenha 2 elementos nº3,
#será eliminado o primeiro nº3

lista.remove(3)
print("Depois do remove: ", lista)


#count (contar qnts vezes o elemento aparece na lista)

print("Qnt de 2 na lista: ", lista.count(2))

#index (diz o índice de um determinado elemento na lista)
print("Indice do elemento 12: ", lista.index(12))

#sort (serve pra ordenar a lista)

lista.sort() #ordem crescente

print(lista)

lista.sort(reverse=True) #ordem decrescente

print(lista)


#Funções de lista

#len (sabe qnts elementos tem na lista)

print(len(lista))


#sum (imprime a soma de lista, soma tds os elementos da lista)

print(sum(lista))

#max (retorna o maior valor da lista)

print("Maior elemento da lista: ", max(lista))

#min (retorna o menor valor da lista)

print("Menor elemento da lista: ", min(lista))