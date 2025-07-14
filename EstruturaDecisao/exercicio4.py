# Faça um programa que verifique se uma letra digitada é vogal ou consoante.

print('Digite uma letra para verificar se é vogal ou consoante')

letra = str(input('Digite uma letra: '))

if letra.upper() == 'A' or letra.upper() == 'E' or letra.upper() == 'I' or letra.upper() == 'O' or letra.upper() == 'U':
    print(f'{letra.upper()} é uma vogal')
else:
    print(f'{letra.upper()} é uma consoante')