import math, random

# EXC 28 - Jogo da Adivinhação

numeroComp = random.randint(0,5)

print('-=-' * 50)
numeroJogador = int(input('Eu sou o computador! Pensei em um número de 0 a 5, agora tente adivinhá-lo, participante: '))
print('-=-' * 50)

if numeroComp == numeroJogador:
    print('Boa, você acertou!')
else: 
    print('Poxa vida, não foi dessa vez, tente novamente!')

    