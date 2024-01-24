import math, random

numero = int(input('Digite seu numero de 1 a 9999: '))

unidade = numero // 1 % 10

dezena = numero // 10 % 10

centena = numero // 100 % 10

milhar = numero // 1000 % 10

print('Analisando seu numero: {}'.format(numero))

print(f'Milhar = {milhar}')

print(f'Centena = {centena}')

print(f'Dezena = {dezena}')

print(f'Unidade = {unidade}')


