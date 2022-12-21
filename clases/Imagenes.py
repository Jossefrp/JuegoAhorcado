import pygame


# Para redimensionar una imagen
def img_redimensionada(img_path, size):
    imagen = pygame.image.load(img_path)
    imagen_redimensionada = pygame.transform.scale(imagen, size)
    return imagen_redimensionada
