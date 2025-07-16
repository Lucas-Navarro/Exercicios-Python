'''
Faça um programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo. 
Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.

Dicas:

Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
Triângulo Equilátero: três lados iguais;
Triângulo Isósceles: quaisquer dois lados iguais;
Triângulo Escaleno: três lados diferentes;
'''

print('De três valores para a construção do triângulo para saber qual tipo é')
lado1 = float(input('Digite o valor do primeiro lado: '))
lado2 = float(input('Digite o valor do segundo lado: '))
lado3 = float(input('Digite o valor do terceiro lado: '))

if lado1 == lado2 and lado1 == lado3 and lado2 == lado3:
    print('Triângulo Equilátero: três lados iguais')
elif lado1 != lado2 and lado1 != lado3 and lado2 != lado3:
    print('Triângulo Escaleno: trêS lados diferentes')
else:
    print('Triângulo Isósceles: quaisque lados iguais')