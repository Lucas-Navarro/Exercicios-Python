# Faça um programa que leia três números e mostre o maior deles:

print('Digite três números e veja o maior entre eles')
num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
num3 = int(input('Digite o terceiro número: '))

if num1 > num2 and num1 > num3:
    print(f'O número {num1} é maior que {num2} e {num3}')
elif num2 > num1 and num2 > num3:
    print(f'O número {num2} é maior que {num1} e {num3}')
else:
    print(f'O número {num3} é maior que {num1} e {num2}')