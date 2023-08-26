preco = float(input('Qual é o Preço do produto? R$'))
produto = preco - (preco * 5 / 100)
print('O produto que custava R${:.2f}, na promoção com desconto de 5% vai custar R${:.2f}.'.format(preco, produto))
