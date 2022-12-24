from clases import Imagenes, Boton, Palabras, Ahorcado
import pygame
import sys


SIZE_SCREEN = (1000, 600)


def pantalla_bienvenida(screen):
    # Imagen fondo
    img = Imagenes.img_redimensionada("./img/Fondos/Inicio.png", SIZE_SCREEN)

    # Fondo
    screen.blit(img, (0, 0))

    path_inicio = "./img/Botones/Inicio/"
    # Imagen PLAY
    size_play = (298, 110)
    img_play_azul = Imagenes.img_redimensionada(
        path_inicio + "Play_azul.png", size_play)
    img_play_rojo = Imagenes.img_redimensionada(
        path_inicio + "Play_rojo.png", size_play)

    play = Boton.Boton(img_play_azul, img_play_rojo,
                       500, 300)
    play.cargar(screen)

    # Movimiento mouse
    play.animacion(screen, pygame.mouse.get_pos())

    # Imagen TITULO
    size_titulo = (500, 170)
    img_titulo = Imagenes.img_redimensionada(
        path_inicio + "Titulo_blanco.png", size_titulo)
    img_titulo_rojo = Imagenes.img_redimensionada(
        path_inicio + "Titulo_rojo.png", size_titulo)
    titulo = Boton.Boton(img_titulo, img_titulo_rojo, 500, 100)
    titulo.cargar(screen)

    # Movimiento titulo
    titulo.animacion(screen, pygame.mouse.get_pos())

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == pygame.MOUSEBUTTONDOWN:
            return play.accion(pygame.mouse.get_pos())

    return True


def pantalla_juego(screen, juego: Ahorcado.Ahorcado):
    img = Imagenes.img_redimensionada(
        "./img/Fondos/Juego.png", SIZE_SCREEN)

    screen.blit(img, (0, 0))
    juego.update(screen, 30, 510)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            a = juego.accion_car(pos)
            if a:
                return juego.verificar(a)
    return True


def main():
    pygame.init()
    screen = pygame.display.set_mode(SIZE_SCREEN)
    pygame.display.set_caption("Juego del ahorcado")

    bienvenida = True
    flag_juego = True

    # Palabra
    juego = Ahorcado.Ahorcado("./db/words.json", "./img/Letras")
    juego.iniciar()

    while True:

        # Pantalla bienvenida
        while bienvenida:
            bienvenida = pantalla_bienvenida(screen)

        # Pantalla juego
        while flag_juego:
            flag_juego = pantalla_juego(screen, juego)
            pygame.display.update()

        screen.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()


if __name__ == "__main__":
    main()
