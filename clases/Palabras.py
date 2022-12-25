import json
from random import choice
from . import Imagenes, Boton
import pygame


class Palabra():
    def __init__(self, db):
        self.palabra = ""
        self.tema = ""
        with open(db, encoding="UTF-8") as file:
            self.data: dict = json.loads(file.read())

    def palabra_aleatoria(self):
        self.tema = choice(list(self.data.keys()))
        self.palabra = choice(self.data.get(self.tema))

    def palabra_tema(self, tema):
        if tema not in self.data.keys():
            self.palabra = ""
        self.tema = tema
        self.palabra = choice(self.data.get(self.tema))


class GraficaPalabra:
    color = (255, 255, 255)

    def __init__(self, palabra: Palabra = "") -> None:
        self.word = palabra
        self.palabra_secreta = list("_"*len(self.word.palabra))

    def iniciar(self, palabra: Palabra):
        self.word = palabra
        self.palabra_secreta = list("_"*len(self.word.palabra))

    def draw_line(self, screen, pos_x, pos_y):
        if len(self.palabra_secreta):
            for i, j in enumerate(self.palabra_secreta):
                inicio = pos_x + 27*(2*i + 1)
                fuente = pygame.font.SysFont(
                    "CaskaydiaCove Nerd Font Mono", 40)
                text = fuente.render(j, True, self.color)
                screen.blit(text, (inicio, pos_y))


class ImagenCaracteres(Boton.Boton):
    abecedario = [chr(i) for i in range(65, 91)]
    abecedario.extend(["Á", "É", "Í", "Ó", "Ú"])
    size_img = (110, 105)

    def __init__(self, caracter, img_1, img_2, pos_x, pos_y):
        self.caracter = caracter
        self.img_1 = Imagenes.img_redimensionada(img_1, self.size_img)
        self.img_2 = Imagenes.img_redimensionada(img_2, self.size_img)
        super().__init__(self.img_1, self.img_2, pos_x, pos_y)


if __name__ == "__main__":
    palabra = Palabra("../db/words.json")
    # palabra.palabra_aleatoria()
    palabra.palabra_tema("Animales")
    print(palabra.tema)
    print(palabra.palabra)
