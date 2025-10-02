def calcFibonacci(n):
  a = 0
  b = 1
  for i in range(3, n + 1):
    c = a + b
    a = b
    b = c
  return b



n = int(input("Digite um numero: "))
fib = calcFibonacci(n)
print(f"O {n}° termo de fibonacci é: {fib}")
