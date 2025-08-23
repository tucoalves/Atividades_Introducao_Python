idade = int(input("Digite a idade: "))

if idade <= 12:
    print("Criança")
elif idade <= 59:
    print("Adulto")
elif idade > 60:
    print("Idoso")