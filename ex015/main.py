dias = int(input("Há quantos dias você alugou o carro? "))
km = int(input("Quantos Km rodados? "))
precoDias = dias*60
precoKm = km*0.15
precoFinal = precoDias+precoKm
print("O preço total é de R${:.2f}".format(precoFinal))