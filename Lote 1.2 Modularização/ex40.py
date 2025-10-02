
def somaPrimo(a,b):
  a,b = comparaNum(a,b)
  for i in range(a,b+1):
    ePrimo = True
    for j in range(2, int(i**0.5)+1):
      if (i % j == 0):
        ePrimo = False
        break
    if(ePrimo):
      print(i)
      
def comparaNum(a,b):
  if(a > b):
    b,a = a,b 
  return a,b


x = int(input("Digite um numero: "))
y = int(input("Digite outro numero: "))

somaPrimo(x,y)