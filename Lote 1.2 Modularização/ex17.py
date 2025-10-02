def calcLitros(tPercurso, vMedia):
  distancia = tPercurso * vMedia
  litros = distancia / 12
  return litros

tempViagem = int(input("Digite o valor de duração da viagem (HH): "))
velMedia = int(input("Digite o valor da velocidade media: (KM/h) "))

litroGasto = calcLitros(tempViagem, velMedia)
print(f"O total de litros gastos é: {litroGasto}")
