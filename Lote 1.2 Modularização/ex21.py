def calcMedia(n1, n2, n3, n4):
  media = (n1 + n2 + n3 + n4) / 4
  return media


def mostraSituacao(n1, n2, n3, n4):
  media = calcMedia(n1, n2, n3, n4)
  if (media < 3):
    return "REPROVADO"
  elif (media < 6):
    return "EXAME"
  else:
    return "Aprovado"

nota1 = float(input("Digite a 1° nota"))
nota2 = float(input("Digite a 2° nota"))
nota3 = float(input("Digite a 3° nota"))
nota4 = float(input("Digite a 4° nota"))

situacao = mostraSituacao(nota1, nota2, nota3, nota4)

print(f"Sua situção é: {situacao}")
