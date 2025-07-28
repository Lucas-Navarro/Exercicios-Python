# Faça um programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números.

numeros = []

for i in range(5):
    numero = int(input('Digite número inteiro: '))
    numeros.append(numero)

numeroMultiplicado = numeros[0] * numeros[1] * numeros[2] * numeros[3] * numeros[4]

print(numeros)
print(f'Soma dos números: {sum(numeros)}\nMultiplicação: {numeroMultiplicado}')