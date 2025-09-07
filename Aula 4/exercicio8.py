while True:
    idade = int(input("Digite a idade (ou -1 para sair): "))
    if idade == -1:
        print("Saindo...")
        break
    elif idade > 0 and idade <= 12:
        print("Criança")
    elif idade >= 13 and idade <= 17:
        print("Adolescente")
    elif idade >= 18 and idade <= 59:
        print("Adulto")
    elif idade >= 60:
        print("Idoso")