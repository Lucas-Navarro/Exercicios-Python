# Faça um programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

print('Digite seu sexo, sendo F - Feminino ou M - Masculino')
sexo = str(input('Digite seu sexo:'))

validacao = sexo.upper()

if validacao.startswith('F') == True:
    print('Seu sexo é feminino')
elif validacao.startswith('M') == True:
    print('Seu sexo é masculino')
else:
    print('Sexo inválido')