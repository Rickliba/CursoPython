import random, math

#EXC 35 - Essas medidas podem formar um triangulo?

l1 = int(input("Por favor, digite a medida do lado 1: "))
l2 = int(input("Por favor, digite a medida do lado 2: "))
l3 = int(input("Por favor, digite a medida do lado 3: "))

if l1 + l2 > l3 and l1 + l3 > l2 and l2 + l3 > l1:
    print("Essas medidas formam um triangulo!")
else:
    print("Essas medidas não formam um triangulo!")

