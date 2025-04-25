''' Exercício Python 22:
Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.
    Resolução:
'''

import pygame
pygame.mixer.init()
pygame.mixer.music.load("C:\\Users\\ranie\\Downloads\\embalo.mp3")
pygame.mixer.music.play()
input('Pressione enter para parar a música')
pygame.mixer.music.stop()
