'''
Funções

O que são e pq utilizar?

Funções usadas anteriormente

> print() - imprime uma msg (int, float, str) no console (terminal, cmd)
> input() - retorna u dado informado pelo usuário (entrada padrão e pode receber uma string)
> len() - recebe uma lista e retorna o tamanho dessa lista 
> max() - retorna o maior valor de uma lista

'''

#Criação de Funções

# >Função inicial

#criar msg de saudação

def saudacao():
    print("Seja bem-vindo(a)!")
    print("Olá, é um prazer ter vc fazendo parte desse curso.")

saudacao()
saudacao()
saudacao()

# >Função com parâmetros

def saudacao(nome):
    print(f"Seja bem-vindo(a), {nome}!")
    print("Olá, é um prazer ter vc fazendo parte deste curso.")

saudacao("Simara")

def saudacao(nome, curso):
    print(f"Seja bem-vindo(a), {nome}!")
    print(f"Olá, é um prazer ter vc fazendo parte deste curso de {curso}.")
    
saudacao("Simara", "Python")
saudacao("Joana", "Javascript")

# >Função com parâmetros default

def saudacao(nome, curso="Python"):
    print(f"Seja bem-vindo(a), {nome}!")
    print(f"Olá, é um prazer ter vc fazendo parte deste curso de {curso}.")
    
saudacao("Simara")

# >Função com retorno

def soma(num1, num2):
    return num1 + num2 #usar retorno apenas no final do código, pois ele encerra após rodar.
resultado = soma(5, 7)
    
print("O resultado da soma é: ", resultado)



def calculadora(num1, num2, operacao="+"):
    if operacao == "+":
        return num1 + num2
    elif operacao == "-":
        return num1 - num2
    
resultado = calculadora(10, 20)

print(resultado)



def calculadora(num1, num2, operacao="+"):
    if operacao == "+":
        return num1 + num2
    elif operacao == "-":
        return num1 - num2
    
resultado = calculadora(10, 20, "-")

print(resultado)