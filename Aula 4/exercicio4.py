par = 0
impar = 0

for i in range(1, 5):
    numero = int(input("Digite um número: "))
    
    if numero % 2 == 0:
        par += 1
    else:
        impar += 1

print("Quantidade de números pares:", par)
print("Quantidade de números ímpares:", impar)