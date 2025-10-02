"""
42. Calcule e mostre a série 1 + 2/3 + 3/5 + ... + 50/99
"""

c = 1
serie = 0
for i in range(1, 51):
  serie += i / c
  c += 2
print(serie)
