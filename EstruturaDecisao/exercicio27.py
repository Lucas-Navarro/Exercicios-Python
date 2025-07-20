'''
Uma fruteira está vendendo frutas com a seguinte tabela de preços:

                Até 5 Kg                Acima de 5 Kg
Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg

Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, receberá ainda um desconto de 10% sobre este total.
Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente.
'''

print('         Até 5kg         Acima de 5kg')
print('Morango  R$2,50 KG       R$ 2,20 KG')
print('Maçã     R$1,80 KG       R$ 1,50 KG')

morango = float(input('Quantos kilos quer de morango? '))
maca = float(input('Quantos quilos quer de maçã? '))

if morango > 5:
    valorTotalMorango = morango * 2.20
else:
    valorTotalMorango = morango * 2.50

if maca > 5:
    valorTotalMaca = maca * 1.80
else:
    valorTotalMaca = maca * 1.50

if valorTotalMaca + valorTotalMorango > 25 or morango + maca > 8:
    valorTotalCompra = (valorTotalMaca + valorTotalMorango) * 0.90
    print(f'Valor Morango: R${valorTotalMorango}\nValor Maçã: R${valorTotalMaca}')
    print(f'Descopnto de 5%\nValor total a pagar: R${valorTotalCompra}')
else:
    valorTotalCompra = (valorTotalMaca + valorTotalMorango)
    print(f'Valor Morango: {valorTotalMorango}\nValor Maçã: R${valorTotalMaca}')
    print(f'Valor total a pagar: R${valorTotalCompra}')