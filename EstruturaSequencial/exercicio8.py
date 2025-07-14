# Faça um programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
# Calcule e mostre o total do seu salário no referido mês.

print('Salário total')
valorHora = float(input('Digite o seu valor da hora: '))
horasTrabalhadas = int(input('Digite o total de horas trabalhadas no mês: '))

salario = valorHora * horasTrabalhadas

print(f'O seu salário total é de R${salario}')
