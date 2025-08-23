ladoa = input("Digite o valor do lado A:")
ladob = input("Digite o valor do lado B:")
ladoc = input("Digite o valor do lado C:")

if ladoa + ladob > ladoc and ladoa + ladoc > ladob and ladob + ladoc > ladoa:
    print("É um triangulo")
else:
    print("Não é um triangulo")