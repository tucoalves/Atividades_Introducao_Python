anos_servico = int(input("Digite o número de anos de serviço: "))

if anos_servico <= 5:
    print("Funcionario Júnior")
elif anos_servico <= 10:
    print("Funcionario Pleno")
elif anos_servico > 10:
    print("Funcionario Sênior")