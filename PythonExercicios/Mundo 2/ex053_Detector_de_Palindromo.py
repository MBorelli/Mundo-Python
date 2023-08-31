"""Exercicio 53: Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, 
desconsiderando os espaços. Exemplos de palíndromos:
APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA."""


frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]
#inverso = ''


'''for letra in range(len(junto) - 1, -1, -1):   # outro formato de fazer o exercico é com o 'for' comentado
    inverso += junto[letra]'''

print(f'O inverso de {junto} é {inverso}')

if inverso == junto:
    print('Temos um Palíndromo!')
else:
    print('A frase digitada não é um palíndromo!')
