"""Exercicio 73: Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol,
na ordem de colocação (temporada 2017). Depois mostre:
a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética.
d) Em que posição está o time da Chapecoense."""

times = ('Corinthians', 'Palmeiras', 'Santos', 'Grêmio', 'Cruzeiro', 'Flamengo', 'Vasco',
         'Chapecoense', 'Atletico-MG', 'Botafogo', 'Atletico-PR', 'Bahia', 'Sao Paulo',
         'Fluminense', 'Sport', 'Vitória', 'Coritiba', 'Avaí', 'Ponte Preta', 'Atletico-GO')

print('-=' * 15)
print(f'Lista de Times do Brasileirao 2017: {times}')
print('-=' * 15)
print(f'Os 5 primeiros sao: {times[:5]}')
print('-=' * 15)
print(f'Os 4 utimos sao: {times[-4:]}')
print('-=' * 15)
print(f'Times em ordem alfabetica: {sorted(times)}')
print('-=' * 15)
print(f'A Chapecoense está na {times.index("Chapecoense")+1}ª posiçao')
