import math, random

#EXC 31 - Cálculo de preço de passagem

distanciaViagem = float(input('Por favor, insira qual a distancia da sua viagem em KM: '))


if distanciaViagem <= 200.0:
    print('Sua passagem tera o custo de R${}'.format(distanciaViagem * 0.50))
else: 
    print('Sua passagem tera o custo de R${}'.format(distanciaViagem * 0.45))

