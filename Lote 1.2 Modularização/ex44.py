def calcPotencia(base, expoente):
  resultado = 1
  for i in range(1, expoente + 1):
    resultado *= base
  return resultado



base = int(input("Digite o valor da base: "))
expoente = int(input("Digite o valor do expoente: "))


potencia = calcPotencia(base, expoente)


print(f"{base} ^ {expoente} = {potencia}")
