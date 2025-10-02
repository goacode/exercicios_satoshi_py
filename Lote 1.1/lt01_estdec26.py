""""
26. Receba 2 números inteiros. Verifique e mostre se o maior número é múltiplo
do menor.
"""

x = int(input("Digite um valor: "))
y = int(input("Digite outro valor: "))

if (x > y and x % y == 0 or y > x and y % x == 0):
    print("O maior é multiplo do menor")
else:
    print("O maior não é multiplo do menor")