'''João, um pescador, comprou um microcomputador para controlar o rendimento diário de seu trabalho. 
Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) 
deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a variável peso (peso de peixes) e 
calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar.
 Imprima os dados do programa com as mensagens adequadas.'''


print('Pesca de peixes')

pesoPeixe = float(input('Digite o peso do peixe: '))

if (pesoPeixe > 50):
    pesoPeixe = pesoPeixe - 50
    multa = pesoPeixe * 4
    print('Multa R$4,00 por quilo')
    print(f'Quantidade de quilos em excesso: {pesoPeixe}KG\nValor da multa a ser pago: R${multa}')
else:
    print('Valor normal, nada de multas')