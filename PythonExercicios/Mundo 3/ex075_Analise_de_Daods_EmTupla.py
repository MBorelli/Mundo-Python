"""Exercico 75: Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla.
No final, mostre:
A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares."""

num = (int(input('digite um número: ')),
       int(input('digite outro número: ')),
       int(input('digite mais um número: ')),
       int(input('digite o último número: ')))

print(f'Você digitou os valores {num}')
print(f'O valor 9 apareceu {num.count(9)} vezes')

if 3 in num:
    print(f'O valor 3 apareceu na {num.index(3) + 1}ª posiçao')
else:
    print('O valor 3 nao foi digitado em nenhuma posiçao')

print('Os valores PARES digitados foram ', end='')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')
