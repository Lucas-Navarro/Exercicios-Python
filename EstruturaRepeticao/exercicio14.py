# Faça um programa que peça 10 números inteiros, calcule e 
# mostre a quantidade de números pares e a quantidade de números impares.

par = []
impar = []

for i in range(10):
    numero = int(input('Digite um número inteiro: '))
    if numero % 2 == 0:
        par.append(numero)
    else: 
        impar.append(numero)

print(f'{len(par)} dos 10 números são par')
print(f'{len(impar)} dos 10 númemros são impar')