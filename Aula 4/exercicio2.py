soma = 0

for i in range(1, 11):
    numero = int(input("Digite um número: "))
    
    if numero > 0:
        soma += numero

print("A soma dos números positivos é:", soma)