def calcSal(qHoras, valHora, desconto, nDependentes):
  salBruto = qHoras * valHora
  salLiq = (salBruto - (salBruto * (desconto / 100)) + (nDependentes * 100))

  return salLiq

horaTrab = int(input("Digite o total de horas trabalhadas: "))
valorHora = int(input("Digite o valor da hora: "))
desconto = int(input("Digite o valor do desconto(%) "))
dependentes = int(input("Digite o total de dependentes: "))

salarioLiq = calcSal(horaTrab, valorHora, desconto, dependentes)
print(f"O salario liquido é: {salarioLiq}")
