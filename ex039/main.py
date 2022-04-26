import time
import sys

#sexo = int(input("Você é homem ou mulher? (homem = 1, mulher = 2) "))

#if sexo == 1:
#    print()
#else:
#    sys.exit()
ano_nasce = int(input("Digite o ano que nasceu: "))
ano_atual = time.localtime()
ano_atual = ano_atual.tm_year
idade = ano_atual - ano_nasce
print("Quem nasceu em {} tem {} anos em {}".format(ano_nasce, idade, ano_atual))

if idade < 18:
    print("Ainda faltam {} ano(s) para o alistamento".format(18 - idade))
    print("Seu alistamento será em {}".format((18 - idade) + ano_atual))
elif idade > 18:
    print("Você já deveria ter se alistado há {} ano(s)".format(idade - 18))
    print("Seu Alistamento seria (ou foi) em {}".format(ano_atual - (idade - 18)))
else:
    print("Você deve se alistar IMEDIATAMENTE")