produto = float(input("Qual é o preço do produto? R$"))
sobra = produto*5/100
produtoDescontado = produto - sobra
print("o produto que custava {}, na promoção com desconto de 5% vai custar {:.2f}".format(produto, produtoDescontado))