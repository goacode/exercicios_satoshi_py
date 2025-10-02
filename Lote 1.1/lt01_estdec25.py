""""
25. Receba a hora de início e de final de um jogo (HH,MM), calcular o tempo do
jogo em horas e minutos, sabendo que o tempo máximo é menor que 24
horas e pode começar num dia e terminar noutro.
"""

horaIni = int(input("Digite as horas que o jogo começou: "))
minIni = int(input("Digite os minutos que o jogo começou: "))

horaFim = int(input("Digite as horas que o jogo terminou: "))
minFim = int(input("Digite os minutos que o jogo terminou: "))

horas = 0

if(horaIni > horaFim):
    horaFim += 24

if(minIni > minFim):
    minFim += 60
    horas -= 1

horas = horaFim - horaIni
minutos = minFim - minIni

print(f"O jogo durou: {horas}h{minutos}min")
