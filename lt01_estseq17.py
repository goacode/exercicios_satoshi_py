""""
17. Calcule a quantidade de litros gastos em uma viagem, sabendo que o
automóvel faz 12 km/l. Receber o tempo de percurso e a velocidade média.
"""

tempo = float(input("Insira o tempo da viagem em horas: "))
velocidade = float(input("Insira a velocidade média em km/h: "))
gasolina = (tempo * velocidade) / 12

print(f"No total foram gastos {gasolina} litros nessa viagem.")