'''
Altere o programa de cálculo do fatorial,
 permitindo ao usuário calcular o fatorial várias vezes e limitando o fatorial a números inteiros positivos e menores que 16.
'''
while True:
    numero = int(input('Digite o número que vai ser fatorado: '))
    numeroGuardar = numero
    for i in range(1,numero):
        numero = numero * i
    if numeroGuardar >= -16 and numeroGuardar <= 16:
        print(f'O fatorial de {numeroGuardar} é {numero}')
    else:
        print('O valor deve estar entre -16 e 16')
        break 
        