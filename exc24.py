import random, math

#Programa que diz se sua cidade começa com 'Santo' ou não

cidade = str(input('Digite o nome da sua cidade: ')).strip()

print('Sua cidade começa com Santo? {}'.format(cidade[:5].upper() == 'SANTO'))

