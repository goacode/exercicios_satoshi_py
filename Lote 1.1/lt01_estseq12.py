""""
12. Receba o ano de nascimento e o ano atual. Calcule e mostre a sua idade e
quantos anos terá daqui a 17 anos.
"""

import datetime

ano_atual = datetime.date.today().year
ano_nascimento = int(input("Digite seu ano de nascimento: "))
idade = ano_atual - ano_nascimento
idade_futura = idade + 17

print(f"Você tem {idade} anos e daqui 17 anos tera {idade_futura} anos.")