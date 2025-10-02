""""
8. Receba o valor de um depósito em poupança. Calcule e mostre o valor
após 1 mês de aplicação sabendo que rende 1,3% a. m.

"""

deposito = float(input("Digite o valor do deposito R$"))
rendimento = deposito * 0.013

print(f"O rendimento total do deposito foi R${rendimento:.2f} totalizando R${deposito + rendimento:.2f} em conta.")
