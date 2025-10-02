def comparaNum(n):
  maior = 0
  menor = 0
  for i in range(1, n+1):
    num = int(input(f"Digite o {i}° numero: "))
    
    if (i == 1):
      maior = num
      menor = num
    else:
      if(num > maior):
        maior = num
      elif(num < menor):
        menor = num
  return maior, menor


maior, menor = comparaNum(10)


print(f"O maior numero é: {maior} e o menor é: {menor}")


        