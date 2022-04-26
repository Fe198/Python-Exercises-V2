casa = float(input("Qual o valor da casa? "))
salario = float(input("Qual o salário do comprador? "))
anos = int(input("Quantos anos de financiamento? "))
prestacao = casa / (anos * 12)

salario30 = 0.3 * salario

if prestacao >= salario30:
    print("Para pagar uma casa de R${:.2f} em {} anos, a prestação será de R${:.2f}\nEmpréstimo NEGADO".format(casa, anos, prestacao))
else:
    print("Para pagar uma casa de R${:.2f} em {} anos, a prestação será de R${:.2f}\nEmpréstimo ACEITO".format(casa, anos, prestacao))