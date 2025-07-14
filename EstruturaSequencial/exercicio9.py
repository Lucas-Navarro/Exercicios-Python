# Faça um programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.

print('Conversor de graus Fahrenheit para Celsius')
temperatura = float(input('Digite a temperatura: '))

conversaoTemperatura = 5 * ((temperatura -32 ) / 9)

print(f'Temperatura em Fehrenheit {conversaoTemperatura}')