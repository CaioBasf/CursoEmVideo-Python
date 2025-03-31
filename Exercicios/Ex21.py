# Fazer um arquivo que rode musica em python

import pygame as py
py.init()
py.mixer.music.load('E:\Workspace\Python\Python - Guanabara\Exercicios\Ex21.mp3')
py.mixer.music.play()
while py.mixer.music.get_busy():
    continue