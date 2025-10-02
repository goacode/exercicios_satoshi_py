"""
44. Receba o número da base e do expoente. Calcule e mostre o valor da potência.
"""

base = int(input("Digite o valor da base: "))
expo = int(input("Digite o valor do expoente: "))
resultado = 1

for i in range(1, expo + 1):
  resultado *= base
print(f"O resultado de {base}^{expo}={resultado}")

