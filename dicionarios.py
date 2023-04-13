# > DICIONÁRIOS

# Criando dicionários

dicionario = {} #dicionário vazio
dicionario = dict()

dicionario = { "nome": "Simara", "idade": 28, "altura": 1.67 }

print(dicionario)
print(dicionario["idade"])

#Adicionando elementos em um dicionário

dicionario["programadora"] = True
print(dicionario)

dicionario["altura"] = 2
print(dicionario)

#Iterando sobre um dicionario
#ele percorre todas as chaves do dicionário e o valor de cada um

for chave in dicionario:
    print(chave, dicionario[chave])

#Testando a existência de uma classe
#saber se uma chave já existe ou não no dicionário

print("peso" in dicionario)
print("altura" in dicionario)
