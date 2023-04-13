'''#Para uma determinada variavel, dentro de uma determinada faixa, 
#faça tal coisa

for variavel in range(5):
    print(variavel)

for variavel in range(1, 10):
    print(variavel)

#vai de 0 até menor do que 10

for variavel in range(1, 12, 3):
    print(variavel)

#pulou de 3 em 3 (ultimo numero que está nos parênteses)
'''
soma = 0

for i in range(1, 4):
    nota = float(input(f"informe a sua nota {i}: "))

soma = soma + nota
print(soma / 3)