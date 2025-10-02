def organizaNum(a,b,c,alr):
  if(alr > c):
    print(a,b,c,alr)
  elif(alr < a ):
    print(alr,a,b,c)
  elif(alr > a and alr < b):
    print(a,alr,b,c)
  else:
    print(a,b,alr,c)
    
    
a = int(input("Digite o menor valor:"))
b = int(input("Digite o valor do meio:"))
c = int(input("Digite o maior valor:"))
aleatorio = int(input("Digite um valor aleatorio:"))

organizaNum(a,b,c,aleatorio)

  