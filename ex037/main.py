numero = int(input("Digite um número inteiro: "))
print("Escolha uma das bases para conversão:")
print("[ 1 ] Converter para BINÁRIO")
print("[ 2 ] Converter para OCTAL")
print("[ 3 ] Converter para HEXADECIMAL")
opcao = int(input("Sua opção:"))

if opcao == 1:
    print("{} para binário é igual a {}".format(numero, bin(numero)))
elif opcao == 2:
    print("{} para octal é igual a {}".format(numero, oct(numero)))
elif opcao == 3:
    print("{} para hexadecimal é igual a {}".format(numero, hex(numero)))
else:
    print("Insira uma opção válida")