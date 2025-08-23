valor = float(input("Digite um valor da compra:"))

if valor > 200:
    valor_final = valor - (valor * 0.20)
    print(f"O valor final com desconto é: R$ {valor_final:.2f}")
elif valor >= 100:
    valor_final = valor - (valor * 0.10)
    print(f"O valor final com desconto é: R$ {valor_final:.2f}")
else:
    print(f"O valor final é: R$ {valor:.2f}")

