'''Exercicio 6: Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.'''

n = int(input('Digite um número: '))

print(f'O dobro de {n} vale {n*2}')
print(f'O triplo de {n} vale {n*3}')
print(f'A raiz de {n} vale {pow(n, (1/2)):.2f}')
