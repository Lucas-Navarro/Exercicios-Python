#Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10. O usuário deve informar 
# de qual numero ele deseja ver a tabuada. A saída deve ser conforme o exemplo abaixo:


print('Tabuada de 1 a 10')
numero = int(input('Digite o número que deseja ver a tabuada: '))

for i in range(1,11):
    tabuada = numero * i
    print(f'{numero} x {i} = {tabuada}')