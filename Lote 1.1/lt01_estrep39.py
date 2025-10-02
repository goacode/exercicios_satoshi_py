"""
39. Calcule a quantidade de grãos contidos em um tabuleiro de xadrez onde:
Casa: 1 2 3 4 ... 64 
Qdte: 1 2 4 8 ... N
"""

graos = 1

for i in range(1, 64):
  graos *= 2
print("O numero de graos na 64° casa é: " + str(graos))
