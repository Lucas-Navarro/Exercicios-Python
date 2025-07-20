#Altere o programa anterior permitindo ao usuário informar as populações e as taxas de 
# crescimento iniciais. Valide a entrada e permita repetir a operação.

pop1 = float(input('Digite o número de habitantes A: '))
cresc1 = float(input('Digite a porcentagem de crescimento por ano da população A: '))
pop2 = float(input('Digite o número de habitantes B: '))
cresc2 = float(input('Digite a porcentagem de crescimento por ano da população B: '))
i = 0

while pop1 < pop2:
    pop1 = pop1 + ((cresc1 / 100) * pop1)
    pop2 = pop2 + ((cresc2 / 100) * pop2)
    i += 1

print(f'Anos necessários para população A passar da B: {i} anos')
print(f'O pais A terá: {pop1} habitantes')
print(f'O pais A terá: {pop2} habitantes')