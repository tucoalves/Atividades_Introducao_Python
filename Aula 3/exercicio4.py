numero = int(input("Digite um numero:"))

if numero > 0 and numero % 2 == 0:
    print(f"{numero} é positivo e par")
elif numero > 0 and numero % 2 != 0:
    print(f"{numero} é positivo e impar")
elif numero < 0 and numero % 2 == 0:
    print(f"{numero} é negativo e par")
elif numero < 0 and numero % 2 != 0:
    print(f"{numero} é negativo e impar")
elif numero == 0:
    print("O numero é zero")