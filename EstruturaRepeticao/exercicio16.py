# Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120

numero = int(input('Digite o número que vai ser fatorado: '))
i = 1
for i in range(numero):
    total = numero * i
    total += total
    print(total)