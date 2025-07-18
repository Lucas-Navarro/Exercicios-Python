'''
Faça um programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque e 
depois informar quantas notas de cada valor serão fornecidas. As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. 
O valor mínimo é de 10 reais e o máximo de 600 reais. O programa não deve se preocupar com a quantidade de notas existentes na máquina.

Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;
Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1.'''

import math
print('Caixa eletrônico\nDigite quanto quer sacar de R$10 - R$600')
sacar = int(input('Digite o valor para sacar: '))
stringInicio = f'Para sacar a quantida de {sacar}, o programa fornece '
if sacar >= 100 and sacar <= 600:
    notasCem = sacar / 100
    stringNotaCem = f'{math.floor(notasCem)} notas de 100, '
    stringConcatenada = stringInicio + stringNotaCem
    print(stringConcatenada)
    notasMenosCem = sacar % 100
    if notasMenosCem >= 50 and notasMenosCem < 100:
        notasCinquenta = notasMenosCem / 50
        stringNotaCinquenta = f'{math.floor(notasCinquenta)} de 50, '
        stringConcatenada = stringInicio + stringNotaCem + stringNotaCinquenta
        print(stringConcatenada)
        if notasCinquenta > 1:
            notasDez = (notasMenosCem % 50) / 10
            stringNotaDez = f'{math.floor(notasDez)} de 10, '
            stringConcatenada = stringInicio + stringNotaCem + stringNotaCinquenta + stringNotaDez
            print(stringConcatenada)
            notasMenosDez = notasMenosCem % 10
            if notasMenosDez >= 5:
                notasCinco = notasMenosDez / 5
                stringNotaCinco = f'{math.floor(notasCinco)} de 5, '
                notasMenosCinco = notasMenosDez % 5
                stringNotaUm = f'{math.floor(notasMenosCinco)} de 1'
                stringConcatenada = stringInicio + stringNotaCem + stringNotaCinquenta + stringNotaDez + stringNotaCinco + stringNotaUm
                print(stringConcatenada)
elif sacar >= 50 and sacar < 100:
    notasCinquenta = sacar / 50
    stringNotaCinquenta = f'{math.floor(notasCinquenta)} de 50, '
    stringConcatenada = stringInicio + stringNotaCinquenta
    print(stringConcatenada)
    if notasCinquenta > 1:
        notasDez = (sacar % 50) / 10
        stringNotaDez = f'{math.floor(notasDez)} de 10, '
        stringConcatenada = stringInicio + stringNotaCinquenta + stringNotaDez
        print(stringConcatenada)
        notasMenosDez = sacar % 10
        if notasMenosDez >= 5:
            notasCinco = notasMenosDez / 5
            stringNotaCinco = f'{math.floor(notasCinco)} de 5, '
            notasMenosCinco = notasMenosDez % 5
            stringNotaUm = f'{math.floor(notasMenosCinco)} de 1'
            stringConcatenada = stringInicio + stringNotaCinquenta + stringNotaDez + stringNotaCinco + stringNotaUm
            print(stringConcatenada)
elif sacar >= 10 and sacar < 50:
    notasDez = sacar / 10
    stringNotaDez = f'{math.floor(notasDez)} de 10, '
    stringConcatenada = stringInicio + stringNotaDez
    print(stringConcatenada)
    notasMenosDez = sacar % 10
    if notasMenosDez >= 5:
        notasCinco = notasMenosDez / 5
        stringNotaCinco = f'{math.floor(notasCinco)} de 5, '
        notasMenosCinco = notasMenosDez % 5
        stringNotaUm = f'{math.floor(notasMenosCinco)} de 1'
        stringConcatenada = stringInicio + stringNotaDez + stringNotaCinco + stringNotaUm
        print(stringConcatenada)
else:
    print('Valor inválido')
    
