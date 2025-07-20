# Faça um programa que leia 5 números e informe o maior número.

numeros = []

for i in range(5):
    numero = int(input('Digite número: '))
    numeros.append(numero)

print(f'O maior número é: {max(numeros)}')