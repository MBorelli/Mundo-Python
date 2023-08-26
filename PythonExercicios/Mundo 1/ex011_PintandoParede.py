'''Exercicio 11: Faça um programa que leia a largura e a altura de uma parede em metros, 
calcule a sua área e a quantidade de tinta necessária para pintá-la, 
sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.'''

largura = float(input('Digite a largura da parede: '))
altura = float(input('Digite a altura da parede: '))
area = largura * altura
print('Sua parede tem dimensão de {}x{} e sua área é de {:.2f}m².'.format(largura, altura, area))
tinta = area / 2
print('Para pintar essa parede, você precisará de {:.2f}l de tinta.'.format(tinta))
