""""
21. Receba 4 notas bimestrais de um aluno. Calcule e mostre a média aritmética.
Mostre a mensagem de acordo com a média:
a. Se a média for >= 6,0 exibir “APROVADO”;
b. Se a média for >= 3,0 E < 6,0 exibir “EXAME”;
c. Se a média for < 3,0 exibir “RETIDO”.
"""

nota1 = float(input("Digite o valor da 1ª nota: "))
nota2 = float(input("Digite o valor da 2ª nota: "))
nota3 = float(input("Digite o valor da 3ª nota: "))
nota4 = float(input("Digite o valor da 4ª nota: "))
media = (nota1 + nota2 + nota3 + nota4)/4

print(f"Sua média final foi: {media}")
if media < 3:
    print("Você está retido!")

elif media < 6:
    print("Você está em exame!")

else:
    print("Você foi aprovado!")
