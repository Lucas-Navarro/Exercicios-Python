# Faça um programa que peça um número e informe se o número é inteiro ou decimal. Dica: utilize uma função de arredondamento.

print('Verifique se é inteiro ou decimal')

numero = float(input('Digite um número: '))

if round(numero) < numero:
    print(f'{numero} é decimal')
else:
    print(f'{numero} é inteiro')