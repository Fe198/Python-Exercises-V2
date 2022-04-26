n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
media = (n1 + n2) / 2
print("A média entre {} e {} é {:.1f}".format(n1, n2, media))

if media < 5.0:
    print("O aluno está reprovado")
elif media >= 5.0 and media < 6.9:
    print("O aluno está em recuperação")
else:
    print("O aluno está aprovado")