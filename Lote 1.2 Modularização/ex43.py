def calcAltura(altA, crescA, altB, crescB):

  crescA /= 100
  crescB /= 100
  anos = 0
  while (altA < altB):
    altA += crescA
    altB += crescB
    anos += 1
  return anos



def comparaNum(a, b):
  if (a > b):
    b, a = a, b
  return a, b


anos = calcAltura(1.1, 3, 1.5, 2)

print(f"Demorou {anos} para Ana passar maria.")
