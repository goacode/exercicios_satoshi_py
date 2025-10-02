"""
34. Receba um número. Calcule e mostre os resultados da tabuada desse número.
"""

n = int(input("Digite um numero: "))

for i in range(1,11):
  print(str(n) + " x " + str(i) + " = " + str(n * i))
