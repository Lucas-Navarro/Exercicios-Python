# Faça um programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.

vogais = ['a' , 'e', 'i', 'o', 'u']
consoantes = []

for i in range(10):
    caracter = str(input('Digite um caracter: '))
    if caracter not in vogais:
        consoantes.append(caracter)

print(f'Foram lidas {len(consoantes)} consoantes')
print(consoantes)