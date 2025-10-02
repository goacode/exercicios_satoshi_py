"""
41. Mostre todas as possibilidades de 2 dados de forma que a soma tenha como resultado 7.
"""

for i in range(1, 7):
  for j in range(1, 7):
    if (i+j == 7):
      print(i,j)