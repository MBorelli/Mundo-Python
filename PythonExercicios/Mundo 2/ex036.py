casa = float(input('Valor da casa: R$'))
salario = float(input('Sálario do comprador: R$'))
ano = int(input('Quantos anos de financiamento? '))
print('-=-' * 20)
valor_mensal = casa / (ano * 12)
minimo = salario * 30 / 100
print('Para pagar uma casa de R${:.2f} em {} anos '
      'a prestação será de R${:.2f}'.format(casa, ano, valor_mensal))
if valor_mensal <= minimo:
    print('Empréstimo pode ser \033[32mCONCEDIDO\033[m!!!')
else:
    print('Empréstimo \033[31mNEGADO\033[m.')
