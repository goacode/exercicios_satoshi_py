"""
33. Receba um número. Calcule e mostre a série 1 + 1/2 + 1/3 + ... + 1/N.
"""

limite = int(input("Digite um numero: "))

serie = sum(1 / i for i in range(1, limite + 1))

print(serie)