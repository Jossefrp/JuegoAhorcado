from . import Palabras, Muñeco
import random
import os


class Ahorcado:
    letras_img = ['ff.png', 'ii.png', 'zz.png', 'rr.png', 'dd.png', 'vv.png', 'hh.png', 'oo.png', 'ee.png', 'a.png', 'bb.png', 'ss.png', 'gg.png',
                  'ww.png', 'nn.png', 'qq.png', 'pp.png', 'tt.png', 'xx.png', 'mm.png', 'yyJPG.png', 'jj.png', 'kkJPG.png', 'cc.png', 'uu.png', 'll.png']
    abecedario = [chr(i) for i in range(65, 91)]
    abecedario.extend(["Á", "É", "Í", "Ó", "Ú"])

    def __init__(self, db, path_img) -> None:
        self.palabra = Palabras.Palabra(db)
        self.muñeco = Muñeco.Muñeco(288, 225)
        self.matrix_caracteres = list()
        self.path_img = path_img
        self.objetos_caracteres = list()

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
                if j in ["Á", "É", "Í", "Ó", "Ú"]:
                    j = "A"
                name = list(filter(lambda n: n.startswith(
                    j.lower()), self.letras_img))

                boton = Palabras.ImagenCaracteres(j, self.path_img + "/2/" + name[0],
                                                  self.path_img + "/2/" + name[0], 600 + 100*x, 170 + 100*y)
                self.objetos_caracteres.append(boton)

    def grafica_matriz(self, screen):
        for boton in self.objetos_caracteres:
            boton.cargar(screen)

    def update(self, screen, pos_x, pos_y):
        self.grafica_palabra.draw_line(screen, pos_x, pos_y)
        self.muñeco.draw_muñeco(screen)
        self.grafica_matriz(screen)

    def accion_car(self, pos):
        for boton in self.objetos_caracteres:
            if not boton.accion(pos):
                self.objetos_caracteres.remove(boton)
                return boton.caracter

    def error(self):
        if self.muñeco.contador >= 5:
            return False
        self.muñeco.contador += 1
        return True

    def acierto(self, character):
        posiciones = [i for i, char in enumerate(
            list(self.palabra.palabra)) if character == char]
        
        for i in posiciones:
            self.grafica_palabra.palabra_secreta[i] = character

    def verificar(self, character):
        print(character)
        if character not in self.palabra.palabra:
            return self.error()
        self.acierto(character)
        return True
