# Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato:
i = 0
produtos = []
preco = []
for i in range(3):
    nomeProduto = str(input('Digite o nome do produto: '))
    precoProduto = float(input('Digite o preço do produto: '))
    produtos.append(nomeProduto)
    preco.append(precoProduto)

print(produtos)
print(preco)    

if preco[0] > preco[1] and preco[0] > preco[2]:
    print(f'Produto mais barato é {produtos[0]}\nPreço: R${preco[0]}')
elif preco[1] > preco[0] and preco[1] > preco[2]:
    print(f'Produto mais barato é {produtos[1]}\nPreço: R${preco[1]}')
else:
    print(f'Produto mais barato é {produtos[2]}\nPreço: R${preco[2]}')

