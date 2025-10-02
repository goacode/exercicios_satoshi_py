"""
38. Receba 100 números inteiros reais. 
Verifique e mostre o maior e o menor valor. Obs.: somente valores positivos.
"""

menor = 0
maior = 0

for i in range(1, 6):
  n = int(input("Digite um numero: "))
  if (i == 1):
    menor = n
    maior = n
  else:
    if (n > maior):
      maior = n
    if (n < menor):
      menor = n
print("O maior numero é: " + str(maior) + " O menor número é: " + str(menor))
