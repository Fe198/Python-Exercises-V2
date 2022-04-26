import random
import time

print("""Suas opções:
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura""")
player = input("Qual é a sua jogada? ")
computer = random.randint(0, 2)

# situacoes que o player vence
if player == 2 and computer == 1:
    print("Jogador vence")
elif player == 1 and computer == 0:
    print("Jogador vence")
elif player == 0 and computer == 2:
    print("Jogador vence")

#situacoes que o player perde
elif player == 1 and computer == 2:
    print("Computador vence")
elif player == 0 and computer == 1:
    print("Computador vence")
elif player == 2 and computer == 0:
    print("Computador vence")
print("o computador jogou {}".format(computer))