celular = input("Digite o número do celular (apenas digitos): ")
if len(celular) == 9 and celular.isdigit():
    print("Número de celular válido.")
else:
    print("Número de celular inválido. Deve conter exatamente 9 dígitos.")