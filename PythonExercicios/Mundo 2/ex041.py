from datetime import date
hoje = date.today().year
nasc = int(input('Ano de nascimento: '))
idade = hoje - nasc
print('O atleta tem {} anos.'.format(idade))
if idade <= 9:
    print('Classificação: MIRIN.')
elif idade <= 14:
    print('Classificação: INFANTIL.')
elif idade <= 19:
    print('Classificação: JUNIOR.')
elif idade <= 25:
    print('Classificação: SÊNIOR.')
elif idade > 25:
    print('Classificação: MASTER.')
