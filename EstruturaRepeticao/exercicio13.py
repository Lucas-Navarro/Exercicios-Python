#Faça um programa que peça dois números, base e expoente, 
# calcule e mostre o primeiro número elevado ao segundo número. 
# Não utilize a função de potência da linguagem.

print('Potência')
base = int(input('Digite o número para base: '))
expoente = int(input('Digite o expoente: '))

for i in range(expoente):
    potencia = base ** expoente

print(potencia)