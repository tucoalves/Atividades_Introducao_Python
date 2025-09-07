soma = 0
N = int(11)

for i in range(1, N):
    numero = int(input("Digite um número: "))
    
    if numero % 5 == 0 and numero > 0:
        soma += numero

print("A soma dos multiplos de 5 é:", soma)