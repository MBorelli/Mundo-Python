"""Exercicio 37: Escreva um programa em Python que leia um número inteiro qualquer 
e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal."""


num = int(input('Digite um número inteiro: '))

print('''Escolha uma das bases para conversão: 
[ 1 ] Converter para BINÁRIO
[ 2 ] Converter para OCTAL
[ 3 ] Converter para HEXADECIMAL''')

opcao = int(input('Sua opção: '))

if opcao == 1:
    print('O núemro {} convertido em BINÁRIO é {}'.format(num, bin(num)[2:]))
elif opcao == 2:
    print('O número {} convertido em OCTAL é {}'.format(num, oct(num)[2:]))
elif opcao == 3:
    print('O número {} convertido em HEXADECIMAL é {}'.format(num, hex(num)[2:]))
else:
    print('A opção {} é invalida. Tente novamente'.format(opcao))
