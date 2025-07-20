'''
Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:

"Telefonou para a vítima?"
"Esteve no local do crime?"
"Mora perto da vítima?"
"Devia para a vítima?"
"Já trabalhou com a vítima?"

O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões 
ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".
'''
respostas = []

print('Respondas as perguntas com SIM ou NÃO')
pergunta1 = str(input('Telefonou para vítima? '))
pergunta2 = str(input('Esteve no local do crime? '))
pergunta3 = str(input('Mora perto da vítima? '))
pergunta4 = str(input('Devia para vítima? '))
pergunta5 = str(input('Já trabalhou vom s vítima? '))

respostas.append(pergunta1)
respostas.append(pergunta2)
respostas.append(pergunta3)
respostas.append(pergunta4)
respostas.append(pergunta5)

if respostas.count('sim') == 2:
    print('Suspeita')
elif respostas.count('sim') > 2 and respostas.count <= 4:
    print('Cúmplice')
elif respostas.count('sim') == 5:
    print('Assasino')
else:
    print('Inocente')