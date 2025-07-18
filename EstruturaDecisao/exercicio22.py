# Faça um programa que peça um número inteiro e determine se ele é par ou impar. Dica: utilize o operador módulo (resto da divisão).

print('Verifique se é impar ou par')
numero = int(input('Digite o número: '))

if numero % 2 == 0:
    print(f'{numero} é par')
else:
    print(f'{numero} é impar')