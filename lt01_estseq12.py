import datetime

ano_atual = datetime.date.today().year
ano_nascimento = int(input("Digite seu ano de nascimento: "))
idade = ano_atual - ano_nascimento
idade_futura = idade + 17

print(f"Você tem {idade} anos e daqui 17 anos tera {idade_futura} anos.")