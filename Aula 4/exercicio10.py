total = 0

while True:
    print("Menu:")
    print("1. Adicionar")
    print("2. Subtrair")
    print("3. Mostrar total")
    print("4. Sair")

    escolha = input("Escolha uma opção (1-4): ")

    if escolha == '1':
        numero = int(input("Digite um número para adicionar: "))
        total += numero
    elif escolha == '2':
        numero = int(input("Digite um número para subtrair: "))
        total -= numero
    elif escolha == '3':
        print("Total atual:", total)
    elif escolha == '4':
        print("Saindo...")
        break