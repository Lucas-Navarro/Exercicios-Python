# Faça um programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a média de cada aluno, 
# imprima o número de alunos com média maior ou igual a 7.0.
alunos = []
medias = []

for i in range(2):
    media = []
    aluno = str(input('Digite seu nome:'))
    alunos.append(aluno)
    for x in range(4):
        nota = float(input('Digite sua nota: '))
        media.append(nota)
    calMedia = sum(nota) / 4
    medias.append(calMedia)
    

print(alunos)
print(medias)