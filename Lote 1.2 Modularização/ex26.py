def verificaMult(a,b):
  if(b > a):
    b,a = a,b
  if(a % b == 0):
    return "Sim"
  else:
    return "Não"


a = int(input("Digite um numero: "))
b = int(input("Digite outro numero: "))


resp = verificaMult(a,b)
print(resp)