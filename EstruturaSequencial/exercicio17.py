'''
Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.

Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
comprar apenas latas de 18 litros;
comprar apenas galões de 3,6 litros;
misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.

'''

metrosQuadrados = float(input('Digite a área em m2 da área a ser pintada: '))

tinta = metrosQuadrados / 6
tintaFolga = tinta * 1.1
qtdLataTinta = tinta / 18
qtdGalaoTinta = tinta / 3.6
valorPagarLata = round(qtdLataTinta) * 80
valorPagarGalao = round(qtdGalaoTinta) * 25
# Latas

if (tinta > 18):
    print(f'Total de tinta a usar: {tinta}L\nLatas de tinta: {round(qtdLataTinta)}\nGalões de tinta: {round(qtdGalaoTinta)}\nValor a pagar Lata: R${valorPagarLata}\nValor a pagar Galão: R${valorPagarGalao}')
else:
    print(f'Total de tinta a usar: {tinta}L\nLatas de tinta: {round(qtdLataTinta)}\nGalões de tinta: {round(qtdGalaoTinta)}\nValor a pagar Lata: R${valorPagarLata}\nValor a pagar Galão: R${valorPagarGalao}')

    
