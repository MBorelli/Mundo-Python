'''Exercicio 14: Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.'''

cel = float(input('Informe a temperatura em °C: '))
far = ((cel * 9) / 5) + 32
print('A temperatura de {:.1f}°C corresponde a {:.1f}°F'.format(cel, far))
