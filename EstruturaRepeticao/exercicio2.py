'''
Faça um programa que 
leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, 
mostrando uma mensagem de erro e voltando a pedir as informações.
'''

while True:
    nomeUser = str(input('Digite um nome de usuário: '))
    senhaUser = str(input('Digite sua senha: '))
    if nomeUser != senhaUser:
        print('Cadastrado com Sucesso')
        break