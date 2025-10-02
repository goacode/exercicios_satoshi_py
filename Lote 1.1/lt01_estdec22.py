""""
22. Receba 2 valores inteiros e diferentes. Mostre seus valores em ordem
crescente.
"""

v1 = int(input("Digite o primeiro valor: "))
v2 = int(input("Digite o segundo valor: "))

if v1 == v2:
    print("[ERRO] Valores iguais, tente novamente!")

elif v1 > v2:
    print(f"{v1} é maior que {v2}")

else:
    print(f"{v2} é maior que {v1}")
