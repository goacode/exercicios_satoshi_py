def calcSerie(n):
  serie = 0
  for i in range(1, n+1):
    serie += 1/i
  return serie

x = int(input("Digite um valor:"))
serie = calcSerie(x)


print(f"A serie de {x} é: {serie}")
