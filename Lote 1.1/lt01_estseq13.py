""""
13. Receba a quantidade de alimento em quilos. Calcule e mostre quantos dias
durará esse alimento sabendo que a pessoa consome 50g ao dia.
"""

comida_kg = float(input("Digite a quantidade de comida que você possui em quilogramas: "))
dias_restantes = comida_kg / 0.05

print(f"Com {comida_kg}kg sua comida durara {dias_restantes:.0f} dias.")