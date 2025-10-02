"""
40. Receba 2 números inteiros. Verifique e mostre todos os números primos existentes entre eles.
"""

a = int(input("Digite  um numero: "))
b = int(input("Digite outro numeri: "))

if(a > b):
  a,b = b,a

for i in range(a, b+1):

  ePrimo = True
  for j in range(2, int(i**0.5) + 1):
    if i % j == 0:
      ePrimo = False
      break
  if(ePrimo):
    print(i)
    