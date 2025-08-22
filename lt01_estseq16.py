horas_trabalhadas =  float(input("Insira o número de horas trabalhadas: "))
valor_hora = float(input("Insirao valor por hora trabalhada: R$"))
desconto_percentual = float(input("Insira o percentual de desconto: %"))
dependentes = int(input("Insira o número de dependentes: "))

salario = horas_trabalhadas * valor_hora
desconto = salario * (desconto_percentual / 100)
salario_liquido = (salario - desconto) + (dependentes * 100)

print(f"Você tem um total de R${salario_liquido:.2f} a receber.")