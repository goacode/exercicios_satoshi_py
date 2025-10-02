def reajusteProd(precoProd, vendaProd):
  if(vendaProd < 500 and precoProd < 30):
    precoProd *= 1.1
  elif(vendaProd < 1000 and precoProd < 80):
    precoProd *= 1.15
  else:
    precoProd *= 0.95
  return precoProd


mediaMensal = int(input("Digite o valor da media mensal do produto:"))
precoAtual = int(input("Digite o valor do preço atual do produto:"))


novoValor = reajusteProd(precoAtual, mediaMensal)


print(f"O novo valor do produto é: {novoValor}")
