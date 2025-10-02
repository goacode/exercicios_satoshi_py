"""
29. Receba o tipo de investimento (1 = poupança e 2  = renda  fixa) e o valor do 
investimento.  Calcule  e  mostre  o  valor  corrigido  em  30  dias  sabendo  que  a 
poupança = 3% e a renda fixa = 5%. Demais tipos não serão considerados. 
"""
tipoInvest = int(
    input("Digite o tipo de investimento: \n1- Poupança\n2- Renda fixa\n"))
invest = int(input("Digite o valor do investimento: "))

if (tipoInvest == 1):
  montante = invest * 1.03
  print("O seu montante depois de 30 dias é: " + str(montante))
elif (tipoInvest == 2):
  montante = invest * 1.05
  print("O seu montante depois de 30 dias é: " + str(montante))
else:
  print("ERRO. Digite um número que condiza com um investimento")
