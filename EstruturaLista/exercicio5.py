# Faça um programa que leia 20 números inteiros e armazene-os num vetor. Armazene os números pares no vetor PAR 
# e os números IMPARES no vetor impar. Imprima os três vetores.
numeros = []
par = []
impar = []

for i in range(20):
    numero = int(input('Digite um número: '))
    numeros.append(numero)
    if numero % 2 == 0:
        par.append(numero)
    else:
        impar.append(numero)

print(numeros)
print(par)
print(impar)

