# Faça um programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.

print('Conversor de graus Celsius para Fahrenheit')
temperatura = float(input('Digite a temperatura: '))
fahrenheit = 32

conversaoTemperatura = (temperatura * 9/5) + 32

print(f'Graus Fahrenheit: {conversaoTemperatura}')