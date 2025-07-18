#Tendo como dados de entrada um arquivo em Gigabytes, construa um algoritmo que faça a conversão para Megabytes e Kilobytes, usando as seguintes fórmulas:

#Para Megabytes: Gigabytes * 1024
#Para Kilobytes: Gigabytes * 1024 * 1024
#Responda o tamanho do arquivo em Megabytes e o tamanho em Kilobytes.

print('Conversor de Gigabytes para Megabytes')
valorMega = float(input('Digite o valor em Gigabytes: '))

print(f'Gigabytes: {valorMega}GB\nMegabytes: {valorMega * 1024}MB\nKilobytes: {(valorMega * 1024) * 1024}KB')