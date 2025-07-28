'''
Faça um programa que peça um número inteiro e 
determine se ele é ou não um número primo. Um número primo é aquele que é divisível somente por ele mesmo e por 1.
'''

while True:
    numero = int(input('Digite um número inteiro: '))
    if numero / numero == 1:
        print(f'{numero} é um número primo')
    else:
        print(f'{numero} é um número composto')
