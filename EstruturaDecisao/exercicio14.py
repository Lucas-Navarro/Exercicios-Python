# Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e 
# calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:

nota1 = float(input('Digite sua primeira nota: '))
nota2 = float(input('Digite sua segunda nota: '))

media = (nota1 + nota2) / 2

if media >= 9 and media == 10:
    print('Média: A')
elif media >= 7.5 and media < 9:
    print('Média: B')
elif media >= 6 and media < 7.5:
    print('Média: C')
elif media >= 4 and media < 6:
    print('Média: D')
else:
    print('Média: E')