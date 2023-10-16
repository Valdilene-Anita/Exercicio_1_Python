print("********************")
print("Bem vindo ao jogo!")
print("*******************")

numero_secreto = 42

chute_str = input("Digite o seu numero: ")

print("Voce digitou" , chute_str)

chute = int(chute_str)

acertou = chute == numero_secreto
maior   = chute > numero_secreto
menor   = chute < numero_secreto

if (acertou):
    print("Você acertou!")
else:
    if (maior):
        print("Você errou! O chute foi maior que o numero secreto")
    elif (menor):
        print("Você errou! O chute foi menor que o numero secreto")

print("Fim do jogo")