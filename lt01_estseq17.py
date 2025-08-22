tempo = float(input("Insira o tempo da viagem em horas: "))
velocidade = float(input("Insira a velocidade média em km/h: "))
gasolina = (tempo * velocidade) / 12

print(f"No total foram gastos {gasolina} litros nessa viagem.")