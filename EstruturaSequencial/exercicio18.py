# Faça um programa que peça o tamanho de um arquivo para download (em MB) 
# e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).

tamanhoArquivo = float(input('Digite o tamanha do arquivo em MB: '))
velocidadeInternet = float(input('Digite a velocidade da internet: '))

tempoDownload = tamanhoArquivo / velocidadeInternet

print(f'Tempo estimado: {tempoDownload}s')

