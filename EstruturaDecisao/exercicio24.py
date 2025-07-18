'''
Faça um programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar. 
O resultado da operação deve ser acompanhado de uma frase que diga se o número é:

par ou ímpar;
positivo ou negativo;
inteiro ou decimal.

'''

num1 = float(input('Digite o primeiro número: '))
num2 = float(input('Digite o segundo número: '))

print('Escolha Uma dessas opções digitando um número\n1- Par ou impar\n2-Positivo ou Negativo\n3-Inteiro ou decimal')
escolha = int(input('Número: '))

if escolha == 1:
    if round(num1) % 2 == 0:
        print(f'{num1} é par')
    else:
        print(f'{num1} é impar')

    if round(num2) % 2 == 0:
        print(f'{num2} é par')
    else:
        print(f'{num2} é impar')
elif escolha == 2:
    if num1 < 0:
        print(f'{num1} é negativo')
    else:
        print(f'{num1} é positivo')
        
    if num2 < 0:
        print(f'{num2} é negativo')
    else:
        print(f'{num2} é positivo')
elif escolha == 3:
    if round(num1) < num1:
        print(f'{num1} é decimal')
    else:
        print(f'{num1} é inteiro')

    if round(num2) < num2:
        print(f'{num2} é decimal')
    else:
        print(f'{num2} é inteiro')
else:
    print('Valor inválido')