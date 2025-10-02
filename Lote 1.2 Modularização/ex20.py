def calcRaiz(a, b, c):
  delta = ((b * b) - 4 * a * c)**0.5

  if (delta >= 0):
    x1 = (-b + delta) / (2 * a)
    x2 = (-b - delta) / (2 * a)
    return x1, x2
  else:
    return "Não tem raiz real"

a = int(input("Digite o valor de a:"))
b = int(input("Digite o valor de b:"))
c = int(input("Digite o valor de c:"))

x1, x2 = calcRaiz(a, b, c)
print(f"Os valores de x1 é: {x1} e o valor de x2 é: {x2}")
