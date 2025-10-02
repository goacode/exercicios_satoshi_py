def calcDif(a, b):
  if (b > a):
    b, a = a, b
  resultado = a - b
  return resultado

a = int(input("Digite um numero: "))
b = int(input("Digite outro numero: "))

dif = calcDif(a, b)

print(f"A diferença do maior para o menor é: {dif}")
