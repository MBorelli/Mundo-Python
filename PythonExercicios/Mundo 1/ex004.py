'''Exercicio 4: Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.'''

a = input('Dgite algo: ')
print(f'O tipo primitivo desse valor é {type(a)}')
print(f'Só tem espaços? {a.isspace()}')
print(f'É um número? {a.isnumeric()}')
print(f'É alfabetico? {a.isalpha()}')
print(f'É alfanumerico? {a.isalnum()}')
print(f'Está em maiúscula? {a.isupper()}')
print(f'Está em minúscula? {a.islower()}')
print(f'Está capitalizado? {a.istitle()}')