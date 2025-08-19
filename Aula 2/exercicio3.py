preco = input("Digite o preço original: ")
desconto = input("Digite o percentual de desconto: ")

print(f"Valor com desconto: {float(preco) * (1 - float(desconto) / 100)}")