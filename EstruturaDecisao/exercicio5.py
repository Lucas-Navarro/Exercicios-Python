'''
Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:

A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
A mensagem "Reprovado", se a média for menor do que sete;
A mensagem "Aprovado com Distinção", se a média for igual a dez.
'''
print('Veja sua média digitando suas duas notas')
nota1 = float(input('Digite sua primeira nota:'))
nota2 = float(input('Digite sua segunda nota: '))

media = (nota1 + nota2) / 2

if media == 10:
    print(f'Média: {media}\nAprovado com Distinção')
elif media >= 7:
    print(f'Média: {media}\nAprovado')
else:
    print(f'Média:{media}\nReprovado')