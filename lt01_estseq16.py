""""
16. Receba a quantidade de horas trabalhadas, o valor por hora, o percentual
de desconto e o número de dependentes. Calcule o salário que serão as
horas trabalhadas x o valor por hora. Calcule o salário líquido (= Salário
Bruto – desconto). A cada dependente será acrescido R$ 100 no Salário
Líquido. Exiba o salário a receber.
"""

horas_trabalhadas =  float(input("Insira o número de horas trabalhadas: "))
valor_hora = float(input("Insirao valor por hora trabalhada: R$"))
desconto_percentual = float(input("Insira o percentual de desconto: %"))
dependentes = int(input("Insira o número de dependentes: "))

salario = horas_trabalhadas * valor_hora
desconto = salario * (desconto_percentual / 100)
salario_liquido = (salario - desconto) + (dependentes * 100)

print(f"Você tem um total de R${salario_liquido:.2f} a receber.")