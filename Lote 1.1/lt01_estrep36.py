"""
36. Receba um número N. Calcule e mostre a série 1 + 1/1! + 1/2! + ... + 1/N!
"""

n = int(input("Digite um numero: "))

resultado = 1
serie = 0
for i in range(1,n+1):
  resultado *= i
  serie += 1 / resultado
  
print("A serie fatorial é: " + str(serie))