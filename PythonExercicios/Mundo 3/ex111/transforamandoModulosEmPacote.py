"""Exercicio 111: Crie um pacote chamado utilidadesCeV que tenha dois módulos internos chamados moeda e dado. 
Transfira todas as funções utilizadas nos desafios 107, 108 e 109 para o primeiro pacote e mantenha tudo funcionando."""


from ultilidadescev import moeda

p = float(input('Digite o preço: R$'))

moeda.resumo(p, 60, 15)

# Observação: acredito por ser editor de código diferente e por ser epocas diferentes da aula do professor, minha resolução ficou diferente da do professor.