import math, random

#EXC 22

nome = str(input('Digite seu nome completo: '))

print(f'Seu nome em maisculas é: {nome.upper()}')

print(f'Seu nome em minusculas é: {nome.lower()}')


print('Seu nome completo tem {} letras'.format(len(nome) - nome.count(' ')))

separaNome = nome.split()

print(f'Seu primeiro nome é: {separaNome[0]} e ele tem {len(separaNome[0])} letras.')




