def calcVelMedia(nVoltas, tamanhoPista, duracao):
  distancia = (tamanhoPista * nVoltas) / 1000
  tempoH = duracao / 60

  velMedia = distancia / tempoH
  return velMedia


nVoltas = int(input("Digite o numero de voltas dadas: "))
extensao = int(input("Digite o valor da extensao (m): "))
duracao = int(input("Digite o valor do tempo gasto (min): "))


velocidade = calcVelMedia(nVoltas, extensao, duracao)
print(f"A velocidade media foi: {velocidade}KM/h")