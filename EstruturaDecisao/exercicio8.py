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
