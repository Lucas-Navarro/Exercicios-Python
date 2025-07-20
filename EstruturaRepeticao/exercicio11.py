# Altere o programa anterior para mostrar no final a soma dos números.


num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
soma = 0


if num1 < num2:
    for i in range(num1, num2):
        soma += i
        print(i)

else:
    for i in range(num2, num1):
        soma += i
        print(i)

print(f'Soma dos números: {soma}')