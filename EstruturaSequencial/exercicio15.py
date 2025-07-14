'''
Faça um programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:

salário bruto.
quanto pagou ao INSS.
quanto pagou ao sindicato.
o salário líquido.
calcule os descontos e o salário líquido, conforme a tabela abaixo:

+ Salário Bruto : R$
- IR (11%) : R$
- INSS (8%) : R$
- Sindicato ( 5%) : R$
= Salário Liquido : R$
'''

valorHora = float(input('Digite o valor da hora: '))
horasTrabalhadas = int(input('Digite as horas trabalhadas por dia: '))
diasTrabalhados = int(input('Digite quantos dias trabalhados: '))

salarioBruto = valorHora * (horasTrabalhadas * diasTrabalhados)

descontoIR = salarioBruto * 0.11
descontoINSS = salarioBruto * 0.08
descontoSindicato = salarioBruto * 0.05

salarioLiquido = salarioBruto - (descontoIR + descontoINSS + descontoSindicato)

print(f'Salário bruto: {salarioBruto}\nDesconto IR:{descontoIR}\nDesconto INSS: {descontoINSS}\nDesconto Sindicato: {descontoSindicato}\nSálario Liquido: {salarioLiquido}')