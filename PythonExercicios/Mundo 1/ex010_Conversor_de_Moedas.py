'''Exercicio 10: Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.'''

brl = float(input('Quanto dinheiro você tem na carteira? R$'))
usd = brl / 3.27
print('Com R${:.2f} você pode comprar US${:.2f}'.format(brl, usd))
