'''
Faça um programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades do mesmo.

Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:

326 = 3 centenas, 2 dezenas e 6 unidades

12 = 1 dezena e 2 unidades

Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16
'''
import math

numero = int(input('Digite um númenro inteiro menor que 1000: '))

if numero >= 100 and numero < 1000:
    centena = numero / 100
    dezena = (numero % 100) / 10
    unidade = (numero % 90) / 1
    print(f'Centenas: {round(centena)}')
    print(f'Dezena: {math.floor(dezena)}')
    print(f'Unidade: {round(unidade)}')
elif numero >= 10 and numero < 100:
    dezena = numero / 10
    unidade = (numero % 10) / 1
    print(f'Dezena: {math.floor(dezena)}')
    print(f'Unidade: {round(unidade)}')
elif numero < 10:
    unidade = numero / 1
    print(f'Unidade: {unidade}')
else:
    print('Valor inválido')

