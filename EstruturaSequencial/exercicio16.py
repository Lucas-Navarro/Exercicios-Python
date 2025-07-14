'''
Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00.
Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.
'''

metrosQuadrados = float(input('Digite a área em m2 da área a ser pintada: '))

tinta = metrosQuadrados / 3

if (tinta > 18):
    qtdLataTinta = tinta / 18
    valorPagar = round(qtdLataTinta) * 80
    print(f'Total de tinta a usar: {tinta}L\nLatas de tinta: {round(qtdLataTinta)}\nValor a pagar: R${valorPagar}')
else:
        print(f'Total de tinta a usar: {tinta}L\nLatas de tinta: 1\nValor a pagar: R$80,00')