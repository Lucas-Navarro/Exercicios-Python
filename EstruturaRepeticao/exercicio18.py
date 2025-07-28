# Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores.
numeros = []
for i in range(1, 11):
    numero = int(input(f'Digite {i} numeros diferentes:')) 
    numeros.append(numero)

print(f'Menor valor: {min(numeros)}\nMaior valor: {max(numeros)}\nSoma dos números: {sum(numeros)}')
