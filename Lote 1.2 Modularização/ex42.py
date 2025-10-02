def calcSerie():
  serie = 0
  c = 1
  for i in range(1,51):
    serie += i / c
    c += 2
  return serie
  
  
calcSerie()