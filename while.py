num_sorteado = 15
num_escolhido = int(input("Informe um num de 1 a 20: "))

if num_sorteado == num_escolhido:
    print("vc acertou!")
else:
    print("tente outra vez!")
    
num_sorteado = 15
num_escolhido = int(input("Informe um num de 1 a 20: "))

while num_escolhido != num_sorteado:
    print("tente outra vez!")

    num_escolhido = int(input("Informe um num de 1 a 20: "))

print("parabéns, vc acertou")
