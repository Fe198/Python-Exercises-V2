import random
import time

print("""Suas opções:
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura""")
player = int(input("Qual é a sua jogada? "))
computer = random.randint(0, 2)

time.sleep(0.5)
print("JO")
time.sleep(1)
print("KEN")
time.sleep(1)
print("PO")
time.sleep(0.25)

if player == 0:
    playerOp = "pedra"
elif player == 1:
    playerOp = "papel"
elif player == 2:
    playerOp = "tesoura"

if computer == 0:
    computerOp = "pedra"
elif computer == 1:
    computerOp = "papel"
elif computer == 2:
    computerOp = "tesoura"

print("=-" * 10)
print("Computador jogou {}".format(computerOp))
print("Player jogou {}".format(playerOp))
print("-=" * 10)

#situação de empate
if player == computer:
    print("EMPATE")

# situacoes que o player vence
if player == 2 and computer == 1:
    print("Jogador vence")
elif player == 1 and computer == 0:
    print("Jogador vence")
elif player == 0 and computer == 2:
    print("Jogador vence")

#situacoes que o player perde
if player == 1 and computer == 2:
    print("Computador vence")
elif player == 0 and computer == 1:
    print("Computador vence")
elif player == 2 and computer == 0:
    print("Computador vence")