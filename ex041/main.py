import time

ano_nasce = int(input("Digite o ano de nascimento: "))
ano_atual = time.localtime().tm_year
idade = ano_atual - ano_nasce

print("O atleta tem {} anos".format(idade))

if idade > 25:
    print("Classificação: Master")
elif idade <= 25 and idade > 19:
    print("Classificação: Sênior")
elif idade <= 19 and idade > 14:
    print("Classificação: Junior")
elif idade <= 14 and idade > 9:
    print("Classificação: Infantil")
elif idade < 9:
    print("Classificação: Mirim")