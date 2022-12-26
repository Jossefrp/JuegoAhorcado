from clases import Imagenes, Boton, Ahorcado, Sonido
import pygame
import sys


SIZE_SCREEN = (1000, 600)
FPS = 60


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

    Sonido.imagen_son(screen)
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
    display_texto(screen, f"Tema: {juego.palabra.tema}",
                  (255, 255, 255), 30, (850, 570))

    juego.update(screen, 30, 510, pygame.mouse.get_pos())
    Sonido.imagen_son(screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            a = juego.accion_imagen(pos)
            if a:
                return juego.verificar(a)
    return True


def display_texto(screen, cadena, color, size_text, pos):
    fuente = pygame.font.SysFont("CaskaydiaCove Nerd Font Mono", size_text)
    texto = fuente.render(cadena, True, color)
    pos_text = texto.get_rect()
    pos_text.centerx = pos[0]
    pos_text.centery = pos[1]
    screen.blit(texto, pos_text)


def win(screen, palabra):
    img_win = Imagenes.img_redimensionada("./img/Fondos/win.png", SIZE_SCREEN)
    screen.blit(img_win, (0, 0))
    display_texto(screen, "La palabra es: ", (255, 255, 255),
                  30, (SIZE_SCREEN[0]/2, 20))
    display_texto(screen, palabra, (89, 250, 40), 60, (SIZE_SCREEN[0] / 2, 70))


def lose(screen, palabra):
    img_win = Imagenes.img_redimensionada("./img/Fondos/lose.png", SIZE_SCREEN)
    screen.blit(img_win, (0, 0))
    display_texto(screen, "La palabra es: ", (255, 255, 255),
                  30, (SIZE_SCREEN[0]/2, 30))
    display_texto(screen, palabra, (245, 29, 29), 70, (SIZE_SCREEN[0] / 2, 90))


def main():
    pygame.init()
    screen = pygame.display.set_mode(SIZE_SCREEN)
    pygame.display.set_caption("Juego del ahorcado")
    Sonido.play_sound()

    bienvenida = True
    flag_juego = True

    # Clock
    clock = pygame.time.Clock()

    # Palabra
    juego = Ahorcado.Ahorcado("./db/words.json", "./img/Letras")
    juego.iniciar()

    verifica = 0
    while True:

        # Pantalla bienvenida
        while bienvenida:
            bienvenida = pantalla_bienvenida(screen)

        # Pantalla juego
        while flag_juego:
            flag_juego = pantalla_juego(screen, juego)
            pygame.display.update()

        if juego.resultado:
            # screen.fill((255, 255, 255))
            win(screen, juego.palabra.palabra)
            while verifica == 0:
                Sonido.win_sound()
                verifica = 1
        else:
            lose(screen, juego.palabra.palabra)
            while verifica == 0:
                Sonido.loser_sound()
                verifica = 1

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()
        clock.tick(FPS)


if __name__ == "__main__":
    main()
