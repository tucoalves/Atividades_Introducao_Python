while True:
    numero = int(input("Digite um número para ver a tabuada (ou 0 para sair):"))

    if numero == 0:
        print("Saindo...")
        break
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")
