def calcSerie():
  serie = 0
  for i in range(1,16):
    if (i % 2 == 0):
      serie += i / (i*i)
    else:
      serie -= i / (i*i)
  return serie


serie = calcSerie()


print(f"A serie é: {serie}")
