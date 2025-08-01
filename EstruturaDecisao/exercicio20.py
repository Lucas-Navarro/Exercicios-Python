'''
Faça um programa para leitura de três notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e presentar:

A mensagem "Aprovado", se a média for maior ou igual a 7, com a respectiva média alcançada;
A mensagem "Reprovado", se a média for menor do que 7, com a respectiva média alcançada;
A mensagem "Aprovado com Distinção", se a média for igual a 10.
'''

print('Veja sua média')
nota1 = float(input('Digite sua primeira nota: '))
nota2 = float(input('Digite sua segunda nota: '))
nota3 = float(input('Digite sua terceira nota: '))

media = (nota1 + nota2 + nota3) / 3

if media == 10:
    print(f'Média: {media}\nStatus: Aprovado com Distinção')
elif media >= 7 and media < 10:
    print(f'Média: {media}\nStatus: Aprovado')
else:
    print(f'Média: {media}\nStatus: Reprovado')