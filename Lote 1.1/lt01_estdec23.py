""""
23. Receba 3 valores obrigatoriamente em ordem crescente e um 4º valor não
necessariamente em ordem. Mostre os 4 números em ordem crescente.
"""

n1 = float(input("Digite o primeiro valor: "))
n2 = float(input("Digite o segundo valor: "))

if n1 > n2:
    print("[ERRO] Valores não estão em ordem crescente!")

else:
    n3 = float(input("Digite o terceiro valor: "))

    if n3 < n2:
        print("[ERRO] Valores não estão em ordem crescente!")
    
    else:
        n4 = float(input("Digite o quarto valor: "))

if n4 > n3:
    print(n1, n2, n3, n4)

elif n4 > n2:
    print(n1, n2, n4, n3)

elif n4 > n1:
    print(n1, n4, n2, n3)

else:
    print(n4, n1, n2, n3)
