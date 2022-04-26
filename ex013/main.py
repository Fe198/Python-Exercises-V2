from re import S


salarioAtual = float(input("Qual é o salário do funcionário? R$"))
aumento = salarioAtual*15/100
salarioAumentado = salarioAtual + aumento
print("O funcionário que ganhava R${} antes, agora com o aumento de 15 porcento, ganha R${:.2f}".format(salarioAtual, salarioAumentado))