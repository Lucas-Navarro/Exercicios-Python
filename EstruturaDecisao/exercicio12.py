'''
Faça um programa para o cálculo de uma folha de pagamento, 
sabendo que os descontos são do Imposto de Renda, que depende do salário bruto (conforme tabela abaixo) e
3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita).
O Salário Líquido corresponde ao Salário Bruto menos os descontos. O programa deverá pedir ao usuário o valor da sua hora e a 
quantidade de horas trabalhadas no mês.

Desconto do IR: - Salário Bruto até 900 (inclusive) - isento - Salário Bruto até 1500 (inclusive) - 
desconto de 5% - Salário Bruto até 2500 (inclusive) - desconto de 10% - Salário Bruto acima de 2500 - desconto de 20%

Imprima na tela as informações, dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220.

'''

print('Calculo da folha de pagamento')
valorHora = float(input('Digite o valor da hora: '))
horasDiarias = int(input('Digite horas trabalhadas por dia: '))
diasTrabalhados = int(input('Digite quantos dias foram trabalhados: '))

salario = valorHora * (horasDiarias * diasTrabalhados)
descontoInss = salario * 0.10
descontoFgts = salario * 0.11

if salario >= 2500:
    descontoIR = salario * 0.20
    salarioLiquido = salario - (descontoFgts + descontoInss + descontoIR)
    print(f'Salário bruto: ({valorHora} * {horasDiarias * diasTrabalhados}):        R${salario}')
    print(f'(-) IR 20%                                                     :        R${descontoIR}')
    print(f'(-) INSS 10%                                                   :        R${descontoInss}')
    print(f'(-) INSS 11%                                                   :        R${descontoFgts}')
    print(f'Total de descontos                                             :        R${descontoInss + descontoFgts + descontoIR}')
    print(f'Salário Líquido                                                :        R${salarioLiquido}')
elif salario >= 1500 and salario < 2500:
    descontoIR = salario * 0.10
    salarioLiquido = salario - (descontoFgts + descontoInss + descontoIR)
    print(f'Salário bruto: ({valorHora} * {horasDiarias * diasTrabalhados}):        R${salario}')
    print(f'(-) IR 10%                                                     :        R${descontoIR}')
    print(f'(-) INSS 10%                                                   :        R${descontoInss}')
    print(f'(-) INSS 11%                                                   :        R${descontoFgts}')
    print(f'Total de descontos                                             :        R${descontoInss + descontoFgts + descontoIR}')
    print(f'Salário Líquido                                                :        R${salarioLiquido}')
elif salario >= 900 and salario < 1500:
    descontoIR = salario * 0.05
    salarioLiquido = salario - (descontoFgts + descontoInss + descontoIR)
    print(f'Salário bruto: ({valorHora} * {horasDiarias * diasTrabalhados}):        R${salario}')
    print(f'(-) IR 20%                                                     :        R${descontoIR}')
    print(f'(-) INSS 10%                                                   :        R${descontoInss}')
    print(f'(-) INSS 11%                                                   :        R${descontoFgts}')
    print(f'Total de descontos                                             :        R${descontoInss + descontoFgts + descontoIR}')
    print(f'Salário Líquido                                                :        R${salarioLiquido}')
else:
    salarioLiquido = salario - (descontoFgts + descontoInss)
    print(f'Salário bruto: ({valorHora} * {horasDiarias * diasTrabalhados}):        R${salario}')
    print(f'(-) IR                                                         :        Isento')
    print(f'(-) INSS 10%                                                   :        R${descontoInss}')
    print(f'(-) INSS 11%                                                   :        R${descontoFgts}')
    print(f'Total de descontos                                             :        R${descontoInss + descontoFgts}')
    print(f'Salário Líquido                                                :        R${salarioLiquido}')