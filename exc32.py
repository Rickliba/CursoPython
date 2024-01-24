import random, math

#EXC 32 - Diga se o ano é bissexto ou não

ano = int(input('Digite o ano que você quer saber: '))

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('Seu ano é bissexto')
else: 
    print('Seu ano não é bissexto')


