# Altere o programa anterior para que ele aceite apenas números entre 0 e 1000.

numeros = []
for i in range(1, 11):
    numero = int(input(f'Digite {i} numeros diferentes:')) 
    while numero > 1000:
            print('Digite um número de 0 a 1000')
            numero = int(input(f'Digite {i} numeros diferentes:')) 
            numeros.append(numero)
    else:
        numeros.append(numero)
print(numeros)
print(f'Menor valor: {min(numeros)}\nMaior valor: {max(numeros)}\nSoma dos números: {sum(numeros)}')