# Faça um programa que peça um valor e mostre na tela se o valor é positivo ou negativo.

print('Digite um número positivo ou negativo')
num1 = float(input('Digite um número:'))

if num1 > 0:
    print(f'Número {num1} é positivo')
else:
    print(f'Número {num1} é negativo')