"""
37. Receba um número inteiro. Calcule e mostre a série de Fibonacci até o seu N’nésimo termo.
"""

n = int(input("Digite o termo de fibonacci que deseja ver: "))

a = 0
b = 1
for i in range(3, n + 1):
  c = a + b
  a = b
  b = c
print("O " + str(n) + " termo de fibonnaci é: " + str(b))
