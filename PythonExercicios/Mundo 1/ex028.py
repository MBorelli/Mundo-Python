'''Exercicio 28: Escreva um programa que faça o computador “pensar” em um número inteiro
 entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. 
 O programa deverá escrever na tela se o usuário venceu ou perdeu.'''

from random import randint
from time import sleep

computador = randint(0, 5) # faz o computador "PENSAR"

print('-=-' * 20)
print('Vou pensar em número entre 0 a 5. tente adivinhar...')
print('-=-' * 20)

jogador = int(input('Em que número eu pensei? ')) # Jogador tenta adivinhar
print('PROCESSANDO...')
sleep(2)

if jogador == computador:
    print('PARABÉNS, você conseguiu me vencer!!!')
else:
    print('GANHEI! Eu pensei no número {} e não no {} !'.format(computador, jogador))
