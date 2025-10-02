"""
45. Calcule e mostre a série 1 – 2/4 + 3/9 – 4/16 + 5/25 + ... + 15/225
"""

serie = 0

for i in range(1, 16):
  if(i % 2 == 0):
    serie += i/(i*i)
  else:
    serie -= (i/(i*i))
print(serie)