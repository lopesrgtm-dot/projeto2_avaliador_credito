def validar_emprestimo(salario_mensal, valor_parcela):
    limite_parcela = salario_mensal * 0.30

    if valor_parcela > limite_parcela:
        return False

    return True

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



    if validar_emprestimo (valor_mensal, salario):
        print("Empréstimo NEGADO: renda insuficiente, parcela acima de 30% da renda")
    else:
        print("Empréstimo APROVADO! Parabéns!")

        