import math, random

salarioAtual = float(input("Digite seu salario atual, por favor: "))

if salarioAtual <= 1250.00:
    print("Como seu salário atual é inferior a 1250 reais, ele será reajustado em 15%. Seu novo salário será R${}".format(salarioAtual + salarioAtual * 0.15))
else: 
    print("Como seu salário atual excede o valor de 1250 reais, seu salário será reajustado em 10%. Seu novo salário será R${}".format(salarioAtual + salarioAtual * 0.10))
