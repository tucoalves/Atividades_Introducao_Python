nota1 = float(input("Digite a primeira nota:"))
nota2 = float(input("Digite a segunda nota:"))
nota3 = float(input("Digite a terceira nota:"))

if nota1 >= 7 and nota2 >= 7 and nota3 >= 7:
    print("Aprovado")
elif nota1 >= 4 and nota2 >= 4 and nota3 >= 4:
    print("Recuperação")
else:
    print("Reprovado")