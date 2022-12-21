import pygame


class Boton(pygame.sprite.Sprite):

    def __init__(self, imagenInicio: pygame.image, imagenFinal, pos_x, pos_y) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.imagenI = imagenInicio
        self.imagenF = imagenFinal
        self.posicion = (pos_x, pos_y)
        self.rect = imagenInicio.get_rect()
        self.rect.centerx = pos_x
        self.rect.centery = pos_y
        self.boton_play = None

    # Animación, si es que el mouse pasa por el la imagen cambia de color
    def animacion(self, screen, pos):
        x, y = pos
        if self.rect.collidepoint(x, y):
            screen.blit(self.imagenF, self.rect)

    # Carga la imagen en screen
    def cargar(self, screen):
        screen.blit(self.imagenI, self.rect)

    # Si es que la posición del mouse colisiona con la imagen retorna falso
    def accion(self, pos):
        x, y = pos
        if self.rect.collidepoint(x, y):
            return False
        return True
