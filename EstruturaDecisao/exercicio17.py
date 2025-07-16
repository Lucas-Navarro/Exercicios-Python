# Faça um programa que peça um número correspondente a um determinado ano e em seguida informe
# se este ano é ou não bissexto.

ano = int(input('Digite um valor de ano (ex: 2019): '))

verificacaoAno = ano % 4

if verificacaoAno == 0:
    print(f'{ano} é bissexto')
else:
    print(f'{ano} não é bissexto')