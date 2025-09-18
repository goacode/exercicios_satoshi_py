""""
20. Receba 3 coeficientes A, B e C de uma equação do 2º grau da fórmula
AX²+BX+C=0. Verifique e mostre a existência de raízes reais e se caso
exista, calcule e mostre.
"""

a = float(input("Digite o valor do coeficiente A: "))
b = float(input("Digite o valor do coeficiente B: "))
c = float(input("Digite o valor do coeficiente C: "))

delta = (b * b) - (4 * a * c)

if delta < 0:
    print("Não existem raizes reais!")

elif delta == 0:
    x1 = (b * (-1))/(2 * a) 
    print(f"Existe uma raiz real que equivale a {x1}")

else:
    x1 = ((b * (-1)) + (delta ** (1/2)))/(2 * a)
    x2 = ((b * (-1)) - (delta ** (1/2)))/(2 * a)
    print(f'Existem duas raízes reais sendo X1 = {x1} E X2 = {x2}' )
