from clases import Imagenes, Boton
from pygame import mixer,mouse #libreria sonido
import pygame
SIZE_SCREEN = (1000, 600)

def play_sound():
    mixer.init(44100, -16,2,2048)
    mixer.music.load("./Sonido/Son.wav")
    mixer.music.play(-1) # Se repite simpre

#LOGO SONIDO
def imagen_son(screen):
    # Imagen Sonido
    size_x=60;
    size_y=50;
    size_son = (size_x, size_y)
    img_son_act = Imagenes.img_redimensionada('./Sonido/1.png', size_son)
    img_son_act1 = Imagenes.img_redimensionada('./Sonido/11.png', size_son)
    img_son_desact = Imagenes.img_redimensionada('./Sonido/2.png', size_son)
    img_son_desact1 = Imagenes.img_redimensionada('./Sonido/22.png', size_son)
    pos_x=880
    pos_y=0
    son_on = Boton.Boton(img_son_act, img_son_act1, 900, 25)
    son_on.cargar(screen)
    son_on.animacion(screen, pygame.mouse.get_pos())
    son_on1 = Boton.Boton(img_son_desact, img_son_desact1, 960, 25)
    son_on1.cargar(screen)
    son_on1.animacion(screen, pygame.mouse.get_pos())
    x, y = mouse.get_pos()
    if (x>pos_x and x<pos_x+size_x and y>pos_y and y<pos_y+size_y):
        for event in pygame.event.get():
            if event.type==pygame.MOUSEBUTTONDOWN:
                play_sound()
                mixer.music.set_volume(1.0)
    else:
        pass
    if (x>pos_x+size_x and x<pos_x+2*size_x and y>pos_y and y<pos_y+size_y):
        for event in pygame.event.get():
            if event.type==pygame.MOUSEBUTTONDOWN:
                play_sound()
                mixer.music.set_volume(0.0)
    else:
        pass

    pygame.display.update()


def win_sound():
    mixer.init(44100, -16,2,2048)
    mixer.music.load("./Sonido/ganador.wav")
    mixer.music.play(1) # Se repite 1 vez

def loser_sound():
    mixer.init(44100, -16,2,2048)
    mixer.music.load("./Sonido/perder.wav")
    mixer.music.play(1) # Se repite 1 vez