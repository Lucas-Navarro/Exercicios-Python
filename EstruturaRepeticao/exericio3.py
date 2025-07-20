'''
Faça um programa que leia e valide as seguintes informações:

Nome: maior que 3 caracteres;
Idade: entre 0 e 150;
Salário: maior que zero;
Estado Civil: 's', 'c', 'v', 'd';


'''

nome = str(input('Digite seu nome: '))
while len(nome) <= 3:
    print('O nome deve ter mais de 3 caracteres')
    nome = str(input('Digite seu nome novamente: '))  


idade = int(input('Infome sua idade: '))
while idade < 0 or idade > 150:
    print('Digite uma idade válida')
    idade = int(input('Informe sua idade novamente: '))

salario = float(input('Digite seu salário: '))
while salario <= 0:
    print('Salário tem que ser maior que zero')
    salario = float(input('Digite seu salário novamente: '))

estadoCivis = ['s', 'c', 'v', 'd']
estadoCivil = str(input(f'Digite seu estado civil: {estadoCivis}'))
while estadoCivil not in estadoCivis:
    print('Estado civil inválido')
    estadoCivil = str(input(f'Digite seu estado civil: {estadoCivis}'))

print('Informações')
print(f'Nome: {nome}\nIdade: {idade}\nSalário: R${salario}\nEstado Civil: {estadoCivil}')