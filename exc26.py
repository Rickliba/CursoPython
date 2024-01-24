import math, random

frase = str(input('Digite sua frase: ')).upper().strip()

print('A Letra A aparece {} vezes na frase'.format(frase.count('A')))
print('A letra A aparece primeiro na posição {}'.format(frase.find('A')+1))
print('A letra A aparece por ultimo na posição {}'.format(frase.rfind('A')+1))

