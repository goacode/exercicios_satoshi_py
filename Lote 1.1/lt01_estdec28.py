""""
28. Receba o preço atual e a média mensal de um produto. Calcule e mostre o
novo preço sabendo que:
Venda Mensal Preço Atual Preço Novo
< 500 < 30 + 10%
>= 500 e < 1000 >= 30 e < 80 +15%
>= 1000 >= 80 - 5%
Obs.: para outras condições, preço novo será igual ao preço atual.
"""

mediaMensal = int(input("Digite o valor da media mensal do produto:"))
precoAtual = int(input("Digite o valor do preço atual do produto:"))

if (mediaMensal < 500 and precoAtual < 30):
  precoNovo = precoAtual * 1.1
elif (mediaMensal < 1000 and precoAtual < 80):
  precoNovo = precoAtual * 1.15
else:
  precoNovo = precoAtual * 0.95

print("O novo preço é: " + str(precoNovo))
