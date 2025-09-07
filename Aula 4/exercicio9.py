tentativas = 0
escolhido = 27

while tentativas < 5:
    numero = int(input("Adivinhe o número (entre 1 e 50): "))

    if numero < 1 or numero > 50:
        print("Número inválido! Tente novamente.")
        continue
    elif numero < escolhido:
        print("Tente um número maior.")
    elif numero > escolhido:
        print("Tente um número menor.")
    else:
        print("Parabéns! Você adivinhou o número.")
        break
    tentativas += 1
else:
    print("Suas tentativas acabaram. O número era:", escolhido)
