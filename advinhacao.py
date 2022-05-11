import random


numero_aleatorio = random.randrange (1,101)

total_de_tentativas = 0


print ("Nível de dificuldade")
print ("Digite: (1)Fácil     (2)Médio     (3)Difícil")



while (True):
    nivel = int(input ("Escolha o seu nível: "))
    if (nivel == 1):
        print("Você possui 10 tentativas")
        total_de_tentativas = 10
        break


    if (nivel == 2):
        print("Você possui 06 tentativas")
        total_de_tentativas = 6
        break
    

    elif (nivel == 3):
        print("Você possui 03 tentativas")
        total_de_tentativas = 3
        break

    else:
        print ("Digite um número válido") 
        continue


for rodada in range (1,total_de_tentativas +1): 
    print (f"Tentativa {rodada} de {total_de_tentativas}")


    chute = int(input("Digite um número inteiro entre 1 e 100: "))

    if (chute <1 or chute >100):
        print ("Digite um número válido")
        continue

    acertou = chute == numero_aleatorio 
    numero_maior = chute > numero_aleatorio
    numero_menor = chute < numero_aleatorio

    if (acertou):
        print ("Parabéns! Você acertou o número.")
        break

    else:
        if (numero_maior):
            print ("O seu chute é maior que o número secreto")

        elif (numero_menor):
            print ("O seu chute é menor que o número secreto")

print ("FIM DE JOGO!")
        


       






