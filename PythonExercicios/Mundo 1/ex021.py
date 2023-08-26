'''Exercicio 21: Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.'''

import pygame

pygame.init()
pygame.mixer.music.load('#')  # subistituir o # pelo nome do arquivo .mp3 desejavel. o mesmo tem que estar na mesma pasta.
pygame.mixer.music.play()
pygame.event.wait()

# este programa não funciona pois falta colocar o arquivo .mp3 para rodar.