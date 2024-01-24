import random, math

#EXC 29 - Radar de velocidade

velociCarro = float(input('Digite a velocidade que o carro estava: '))

velocidadeMax = 80.0

if velociCarro > velocidadeMax: 
    print('Tava rapido demais campeão, de quebra ainda toma esses R${} de multa aí'.format((velociCarro - velocidadeMax) * 7.00))
else: 
    print('Boa, estava dentro do limite da via, continue assim!')
