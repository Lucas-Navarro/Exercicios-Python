# Faça um programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.

print('Programa que calcula a área do quadrado')
ladoQuadrado = float(input('Digite o valor do lado do quadrado: '))

areaQuadrado = ladoQuadrado * ladoQuadrado

dobroArea = areaQuadrado * areaQuadrado

print(f'Área do quadrado: {areaQuadrado}m2\nDobro da área do quadrado: {dobroArea}m2')