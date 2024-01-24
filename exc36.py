import math, random

#EXC 36 - Financiamento de uma Casa

salario = float(input("Digite o valor do seu salário, por favor: "))

valorImóvel = float(input("Agora digite o valor do imóvel que você deseja, por favor: "))

qtdAnos = int(input("Agora, por fim, informe em quantos anos você pretende pagar o imóvel: "))

qtdParcelas = qtdAnos * 12

valorParcela = valorImóvel / qtdParcelas

if valorParcela > salario * 0.3:
    print("Infelizmente, nessa quantidade de anos, não é possível financiar este imóvel.")
else: 
    print("O financiamento foi aprovado! O valor da parcela fica em R${:.2f} e deve ser pago em {} parcelas!".format(valorParcela, qtdParcelas))
