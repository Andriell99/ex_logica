preco = float(input('Ensira o valor do produto: '))
percent = preco*0.05
desconto = preco-percent
print('com os 5% de desconto o preco de {} ficara por {:.2f}'.format(preco,desconto))