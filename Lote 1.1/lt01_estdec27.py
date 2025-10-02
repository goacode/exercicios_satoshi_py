""""
27. Receba o número de voltas, a extensão do circuito (em metros) e o tempo de
duração (minutos). Calcule e mostre a velocidade média em km/h
"""

nVoltas = int(input("Digite o numero de voltas dadas: "))
extensao = int(input("Digite o valor da extensao (m): "))
duracao = int(input("Digite o valor do tempo gasto (min): "))

percurso = (extensao * nVoltas) / 1000
duracaoH = duracao / 60

velMedia = percurso / duracaoH

print("A velocidade media do percurso em KM/h é: " + str(velMedia))
