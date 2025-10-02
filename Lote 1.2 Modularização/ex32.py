def calcFatorial(n):
  fat = 1
  for i in range (1, n+1):
    fat *= i
  return fat


x = int(input("Digite um valor: "))
fatorial = calcFatorial(x)
print(f"O fatorial de {x} é: {fatorial}")
