'''
O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:

                Até 5 Kg                Acima de 5 Kg
File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg

Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção, porém não há limites para a quantidade de carne 
por cliente. 
Se compra for feita no cartão Tabajara o cliente receberá ainda um desconto de 5% sobre o total da compra. 
Escreva um programa que peça o tipo e a quantidade de carne comprada pelo usuário e gere um cupom fiscal,
 contendo as informações da compra: tipo e quantidade de carne, preço total, tipo de pagamento, valor do desconto e valor a pagar.

'''

print('            Até 5kg         Acima de 5kg')
print('File Duplo  R$4,90 KG       R$ 5,80 KG')
print('Alcatra     R$5,90 KG       R$ 6,80 KG')
print('Picanha     R$6,90 KG       R$ 7,80 KG')

tipoCarne = str(input('Qual das carne voce vai levar: '))
qtdCarne = float(input('Quantos quilos? '))

if tipoCarne == 'File Duplo':
    if qtdCarne <= 5:
        totalCarne = qtdCarne * 4.90
    else:
        totalCarne = qtdCarne * 5.90
elif tipoCarne == 'Alcatra':
    if qtdCarne <= 5:
        totalCarne = qtdCarne * 5.90
    else:
        totalCarne = qtdCarne * 6.80
elif tipoCarne == 'Picanha':
    if qtdCarne <= 5:
        totalCarne = qtdCarne * 6.90
    else:
        totalCarne = qtdCarne * 7.80
else:
    print('Carne escrita incorretamente')

cartao = str(input('Compra vai ser passa no cartão Tabajara? '))

if cartao == 'SIM':
    totalPagar = (totalCarne) - (totalCarne * 0.05)
    print(f'Carne: {tipoCarne}\nQuantidade Carne: {qtdCarne}KG')
    print(f'Tipo de pagamento: Cartão Tabajara\nDesconto de 5%\nValor total a pagar: {totalPagar}')
else:
    totalPagar = totalCarne
    print(f'Carne: {tipoCarne}\nQuantidade Carne: {qtdCarne}KG')
    print(f'Tipo de pagamento: Cartão\nValor total a pagar: {totalPagar}')