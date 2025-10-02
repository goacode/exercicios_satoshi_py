"""
43. Calcule e mostre quantos anos serão necessários para que Ana seja maior que Maria sabendo que
Ana tem 1,10 m e cresce 3 cm ao ano e Maria tem 1,5 m e cresce 2 cm ao ano.
"""

altAna = 1.1
crescAna = 3

altMaria = 1.5
crescMaria = 2
anos = 0

while altAna <= altMaria:
  altAna += (crescAna / 100)
  altMaria += (crescMaria / 100)
  anos += 1
print("Ana demorara " + str(anos) + " Para passar Maria")
