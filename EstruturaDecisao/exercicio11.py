'''
As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que 
calculará os reajustes. Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:

salários até R$ 280,00 (incluindo) : aumento de 20%
salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
o salário antes do reajuste;
o percentual de aumento aplicado;
o valor do aumento;
o novo salário, após o aumento.
'''

print('Aumento de salário')
salario = float(input('Digite seu salário: '))

if salario >= 1500:
    valorAumento = salario * 0.05
    salarioAumento = salario + valorAumento
    print(f'Salário antes do ajuste: R${salario}\nPercentual de aumento: 5%')
    print(f'Valor do aumento: R${valorAumento}\nNovo salário: R${salarioAumento}')
elif salario >= 700 and salario < 1500:
    valorAumento = salario * 0.10
    salarioAumento = salario + valorAumento
    print(f'Salário antes do ajuste: R${salario}\nPercentual de aumento: 10%')
    print(f'Valor do aumento: R${valorAumento}\nNovo salário: R${salarioAumento}')
elif salario >= 280 and salario < 700:
    valorAumento = salario * 0.15
    salarioAumento = salario + valorAumento
    print(f'Salário antes do ajuste: R${salario}\nPercentual de aumento: 15%')
    print(f'Valor do aumento: R${valorAumento}\nNovo salário: R${salarioAumento}')
else:
    valorAumento = salario * 0.20
    salarioAumento = salario + valorAumento
    print(f'Salário antes do ajuste: R${salario}\nPercentual de aumento: 20%')
    print(f'Valor do aumento: R${valorAumento}\nNovo salário: R${salarioAumento}')