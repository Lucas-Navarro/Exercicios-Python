# Faça um programa que peça o raio de um círculo, calcule e mostre sua área:
import math 

print('Programa que calcula a área do círculo')
raio = float(input('Digite o valor do raio: '))

areaCirculo = math.pi * (raio * raio)

print(f'Área do círculo: {areaCirculo}')
