def calcInvest(tipoInvest, investimento):
  if (tipoInvest == 1):
    investimento *= 1.03
  else:
    investimento *= 1.05
  return investimento



tipoInvest = int(
    input("Digite o tipo de investimento: \n1- Poupança\n2- Renda fixa\n"))
invest = int(input("Digite o valor do investimento: "))


novoValor = calcInvest(tipoInvest, invest)


print(f"Seu montante depois de 1 mes é: {novoValor}")
