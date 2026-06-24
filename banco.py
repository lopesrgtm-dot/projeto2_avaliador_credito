print("Bem-vindo ao Banco Python")

salario = float(input("Salário Mensal R$: "))
idade = int(input("Idade: "))

if idade <18 :
    print("Empréstimo negado por idade")
else:
    print("Idade aprovada, prosseguindo..")
    emprestimo = float(input("Digite o valor do emprestimo R$: "))
    parcelas = float(input("Quantas parcelas: "))
    valor_mensal = emprestimo / parcelas
    print(f" valor mensal das parcelas R$: {valor_mensal}")

    sparceleas = salario * 0.30 #identifica o valor de 30% do salario

    if parcelas > sparceleas:
        print("Empréstimo NEGADO (renda insuficiente)")
    else:
        print("Empréstimo APROVADO! Parabéns!")

        