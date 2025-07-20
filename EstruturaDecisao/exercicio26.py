'''
Um posto está vendendo combustíveis com a seguinte tabela de descontos:

Álcool:

até 20 litros: desconto de 3% por litro
acima de 20 litros: desconto de 5% por litro
Gasolina: - até 20 litros: desconto de 4% por litro - acima de 20 litros: desconto de 6% por litro

Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina), 
calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.
'''

print('Posto de gasolina')
combustivel = str(input('Você quer Álcool ou Gasolina? '))
litros = float(input('Quantos litros? '))

if combustivel.startswith('A') == True:
    if litros <= 20:
        totalPagar = (litros * 1.9) - (litros * 0.03)
        print(f'Litros: {litros}L\nDesconto de 3%\nTotal a pagar: R${totalPagar}')
    else:
        totalPagar = (litros * 1.9) - (litros * 0.05)
        print(f'Litros: {litros}L\nDesconto de 5%\nTotal a pagar: R${totalPagar}')
elif combustivel.startswith('G') == True:
    if litros <= 20:
        totalPagar = (litros * 2.50) - (litros * 0.04)
        print(f'Litros: {litros}\nDesconto de 4%\nTotal a pagar: R${totalPagar}')
    else:
        totalPagar = (litros * 2.50) - (litros * 0.06)
        print(f'Litros: {litros}\nDesconto de 6%\nTotal a pagar: R${totalPagar}')   
else:
    print('Valor inválido')