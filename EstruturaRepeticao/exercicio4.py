'''
Supondo que a população de um país A seja da ordem de 80_000 habitantes
com uma taxa anual de crescimento de 3% e que a população de B 
seja 200_000 habitantes com uma taxa de crescimento de 1.5%. 
Faça um programa que calcule e escreva o número de anos necessários 
para que a população do país 
A ultrapasse ou iguale a população do país B, 
mantidas as taxas de crescimento.
'''

pop1 = 80.000
pop2 = 200.000
i = 0

while pop1 < pop2:
    pop1 = pop1 + (pop1 * 0.03)
    pop2 = pop2 + (pop2 * 0.015)
    i += 1

print(f'Anos necessários para população A passar da B: {i} anos')
print(f'O pais A terá: {pop1} habitantes')
print(f'O pais A terá: {pop2} habitantes')