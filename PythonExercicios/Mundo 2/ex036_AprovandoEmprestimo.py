"""Exercicio 36: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. 
Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
 A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado."""


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
