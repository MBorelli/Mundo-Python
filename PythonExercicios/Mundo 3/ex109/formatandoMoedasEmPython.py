"""Exercicio 109: Modifique as funções que form criadas no desafio 107 
para que elas aceitem um parâmetro a mais, 
informando se o valor retornado por elas vai ser ou não formatado pela função moeda(), 
desenvolvida no desafio 108."""


from moeda import metade, dobro, aumentar,diminuir, moeda

p = float(input('Digite o preço: R$'))

print(f'A metade de {moeda(p)} é {moeda(metade(p))}')
print(f'O dobro de {moeda(p)} é {moeda(dobro(p))}')
print(f'Aumentando 10%, temos {moeda(aumentar(p, 10))}')
print(f'Diminuindo 13%, temos {moeda(diminuir(p, 13))}')

# Observação: acredito por ser editor de código diferente e por ser epocas diferentes da aula do professor, minha resolução ficou diferente da do professor.