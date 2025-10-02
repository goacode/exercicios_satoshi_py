"""
35. Receba 2 números inteiros, verifique qual o maior entre eles. 
Calcule e mostre o resultado da somatória dos números ímpares entre esses valores.
"""

a = int(input("Digite um numero: "))
b = int(input("Digite outro numero: "))

soma = 0

if(a > b):
  maior = a
  menor = b
else:
  maior = b
  menor = a

for i in range(menor,maior+1):
  if(i % 2 == 1):
    soma += i
print("O valor da somatoria é: " + str(soma))
