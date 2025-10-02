def calculaGrao():
  graos = 1
  for i in range(1, 64):
    graos *= 2
  return graos



print(f"O total de graos na 64° casa é: {calculaGrao()}")