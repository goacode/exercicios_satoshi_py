def calcTempoJogo(hIni, mIni, hFim, mFim):
  horas = 0
  if(hIni > hFim):
    hFim += 24
  if(mIni > mFim):
    mFim += 60
    horas -= 1
  horas = hFim - hIni
  minutos = mFim - mIni

  return horas, minutos
  
horaIni = int(input("Digite as horas que o jogo comecou (HH):"))
minIni = int(input("Digite os minutos que o jogo comecou (MM):"))

horaFim = int(input("Digite as horas que o jogo terminou (HH): "))
minFim = int(input("Digite os minutos que o jogo terminou (MM)"))

tempoH, tempoM = calcTempoJogo(horaIni, minIni, horaFim, minFim)

print(f"O jogo durou: {tempoH}:{tempoM} horas")