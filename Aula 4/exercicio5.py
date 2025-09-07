maior = 0
menor = 0
total = 0
n = 0

while True:
    nota = float(input("Digite uma nota (ou -1 para sair): "))
    
    if nota == -1:
        break
    elif nota < 0 or nota > 10:
        print("Nota inválida. Digite uma nota entre 0 e 10.")
        continue
    elif nota > maior:
        maior = nota
    elif nota < menor or menor == 0:
        menor = nota

    total += nota
    n += 1

print("Maior nota:", maior)
print("Menor nota:", menor)
print("Média das notas:", total / (n))