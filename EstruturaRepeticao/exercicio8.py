# Faça um programa que leia 5 números e informe a soma e a média dos números.

numeros = []

for i in range(5):
    numero = float(input('Digite o número: '))
    numeros.append(numero)

media = sum(numeros) / 5

print(f'Média: {media}')

