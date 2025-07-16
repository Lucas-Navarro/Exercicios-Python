'''
Faça um programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. 
Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.
'''

print('Digite o turno que você estuda')
print('M - MATUTINO / V - VESPERINO / N - NOTURNO')

turno = str(input('Digite o turno: '))

upperTurno = turno.upper()

if upperTurno.startswith('M') == True:
    print('Bom dia')
elif upperTurno.startswith('V') == True:
    print('Boa tarde')
elif upperTurno.startswith('N') == True:
    print('Boa noite')
else:
    print('Valor inválido')

