""""
15. Receba os valores de 2 catetos de um triângulo retângulo. Calcule e mostre
a hipotenusa.
"""

cateto1 = float(input("Digite o primeiro cateto: "))
cateto2 = float(input("Digite o segundo cateto: "))

hipotenusa = ((cateto1 * cateto1) + (cateto2 * cateto2)) ** (1/2)

print(f"A hipotenusa é igual a {hipotenusa}")