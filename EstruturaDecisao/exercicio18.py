# Faça um programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data 
# válida.

dia = int(input('Digite um dia do mês: '))
mes = int(input('Digite o mês do ano: '))
ano = int(input('Digite ano válido: '))

if dia <= 30 and dia > 0:
    if mes > 0 and mes < 12:
        print(f'{dia}/{mes}/{ano}')
    else:
        print('Mês inválido')
else:
    print('Dia inválido')
    