from . import Palabras, Muñeco
import random


class Ahorcado:
    abecedario = [chr(i) for i in range(65, 91)]
    abecedario.extend(["Á", "É", "Í", "Ó", "Ú"])

    def __init__(self, db, path_img) -> None:
        self.palabra = Palabras.Palabra(db)
        self.muñeco = Muñeco.Muñeco(288, 225)
        self.matrix_caracteres = list()
        self.path_img = path_img
        self.objetos_caracteres = list()
        self.resultado = bool()

    def iniciar(self):
        self.palabra.palabra_aleatoria()
        self.grafica_palabra = Palabras.GraficaPalabra(self.palabra)
        self.muñeco.contador = 0

        # Caracteres que apareceran en pantalla
        def llenar_letras(letras):
            if len(letras) >= 16:
                return letras
            letras.add(random.sample(self.abecedario, 1)[0])
            return llenar_letras(letras)

        letras_mostrar = set(list(self.palabra.palabra))
        llenar_letras(letras_mostrar)
        letras_mostrar = list(letras_mostrar)
        self.matrix_caracteres = [letras_mostrar[x:x+4]
                                  for x in range(0, 16, 4)]

        # Cargar imagenes de caracteres
        for x, i in enumerate(self.matrix_caracteres):
            for y, j in enumerate(i):
                boton = Palabras.ImagenCaracteres(j, self.path_img + "/1/" + j.lower() + ".png",
                                                  self.path_img + "/2/" + j.lower() + ".png", 600 + 100*x, 170 + 100*y)
                self.objetos_caracteres.append(boton)

    def grafica_matriz(self, screen):
        for boton in self.objetos_caracteres:
            boton.cargar(screen)

    def update(self, screen, pos_x, pos_y, pos_mouse):
        self.grafica_palabra.draw_line(screen, pos_x, pos_y)
        self.muñeco.draw_muñeco(screen)
        self.grafica_matriz(screen)
        for boton in self.objetos_caracteres:
            boton.animacion(screen, pos_mouse)

    def accion_imagen(self, pos):
        for boton in self.objetos_caracteres:
            if not boton.accion(pos):
                self.objetos_caracteres.remove(boton)
                return boton.caracter

    def error(self):
        if self.muñeco.contador >= 5:
            self.resultado = False
            return False
        self.muñeco.contador += 1
        return True

    def acierto(self, character):
        posiciones = [i for i, char in enumerate(
            list(self.palabra.palabra)) if character == char]

        for i in posiciones:
            self.grafica_palabra.palabra_secreta[i] = character

        if "".join(self.grafica_palabra.palabra_secreta) == self.palabra.palabra:
            self.resultado = True
            return False

        return True

    def verificar(self, character):
        if character not in self.palabra.palabra:
            return self.error()
        return self.acierto(character)
