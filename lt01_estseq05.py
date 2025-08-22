a = float(input("Digite o valor do coeficiente A: "))
b = float(input("Digite o valor do coeficiente B: "))
c = float(input("Digite o valor do coeficiente C: "))

delta = (b * b) - (4 * a * c)

x1 = ((b * (-1)) + (delta ** (1/2))) / (2 * a)
x2 = ((b * (-1)) - (delta ** (1/2))) / (2 * a)

print(f"As raizes da equação são {x1} e {x2}.")
