dia = int(input('Quantos dias alugado? '))
km = float(input('Quantos Km rodados? '))
pago = (60 * dia) + (0.15 * km)
print('O total a pagar é de R${:.2f}'.format(pago))
