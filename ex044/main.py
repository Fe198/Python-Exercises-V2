print("========== LOJAS LIMA ===========")
preco = float(input("Preço das compras: R$"))
print("""FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão""")
opcao = int(input("Digite a sua opção:"))

if opcao == 1:
    print("Por você pagar à vista no dinheiro, o preço fica R${:.2f}".format(preco * 0.9))
elif opcao == 2:
    print("Por você pagar à vista no cartão, o preço fica R${:.2f}".format(preco * 0.95))
elif opcao == 3:
    print("Sua compra será parcelada em 2x de R${:.2f} sem juros".format(preco/2))
    print("Por você pagar 2x no cartão, o preço fica R${:.2f}".format(preco))
elif opcao == 4:
    parcelas = int(input("Quantas parcelas? "))
    precop = preco * 1.2
    print("Sua compra será parcelada em {}x de R${:.2f} com juros".format(parcelas, precop/parcelas))
    print("Sua compra de R${:.2f} ficará R${:.2f} no final".format(preco, precop))
else:
    print("Opção inválida")
