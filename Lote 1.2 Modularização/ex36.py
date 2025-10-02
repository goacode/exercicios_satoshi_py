def serieFat(n):
  fat = 1
  serie = 0
  for i in range(1, n+1):
    fat *= i
    serie += 1 / fat
  return serie


x = int(input("Digite o numero: "))
serie = serieFat(x)
print(f"A serie fatorial é: {serie}")