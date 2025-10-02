def somaImpar(a,b):
  soma = 0
  a,b = comparaNum(a,b)
  for i in range(a,b+1):
    if(i % 2 == 1):
      soma += i
  return soma

def comparaNum(a,b):
  if(a > b):
    a,b = b,a
  return a,b


x = int(input("Digite um numero: "))
y = int(input("Digite outro numero: "))

soma = somaImpar(x,y)
print(soma)
