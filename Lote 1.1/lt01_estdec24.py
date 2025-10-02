""""
24. Receba um valor inteiro. Verifique e mostre se é divisível por 2 e 3.
"""

n =  int(input("Digite um numero: "))

if(n % 2 == 0 and n % 3 == 0):
    print(f"O numero é divisivel por 2 e  3")
else:
    print(f"O numero não é divisivel por 2 e 3")
