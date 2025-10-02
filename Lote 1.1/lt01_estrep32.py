"""
32. Receba um número inteiro. Calcule e mostre o seu fatorial.
"""

limite = int(input("Digite um numero: "))

resultado = 1
i = 1

while i <= limite:
  resultado *= i
  i += 1
print("O fatorial desse numero é: " + str(resultado))
