# Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120

numero = int(input('Digite o número que vai ser fatorado: '))
numeroGuardar = numero

for i in range(1,numero):
    numero = numero * i

print(f'O fatorial de {numeroGuardar} é {numero}')