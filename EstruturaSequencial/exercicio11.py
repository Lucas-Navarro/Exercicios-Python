#Faça um programa que peça 2 números inteiros e um número real. Calcule e mostre:

# O produto do dobro do primeiro com metade do segundo .
# soma do triplo do primeiro com o terceiro.
# O terceiro elevado ao cubo.

valor1 = int(input('Digite um número inteiro: '))
valor2= int(input('Digite o segundo número inteiro: '))
valorReal = float(input('Digite um número real: '))

mod1 = valor1 * valor1 + (valor2 / 2)
mod2 = (valor1 * valor1 * valor1) + valorReal
mod3 = valorReal ** 3

print(mod1)
print(mod2)
print(mod3)