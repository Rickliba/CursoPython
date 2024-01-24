import random, math

#exc 27 - Mostre o primeiro e ultimo nome

nome = str(input('Digite seu nome completo, por favor: '))

nomeSeparado = nome.split()

print('Prazer em te conhecer, seu primeiro nome é {} e seu ultimo nome é {}'.format(nomeSeparado[0], nomeSeparado[len(nomeSeparado)-1]))