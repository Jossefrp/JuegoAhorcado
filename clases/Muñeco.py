import pygame


class Muñeco:
    color = (255, 255, 255)

    contador = 0

    def __init__(self, pos_x, pos_y) -> None:
        self.x = pos_x
        self.y = pos_y
        self.r = 30
        self.pos_figura = [
            ((self.x, self.y + self.r), (self.x, self.y + 5*self.r)),  # |,
            ((self.x - 50, self.y + self.r), (self.x, self.y + 2*self.r)),  # \
            ((self.x, self.y + 2*self.r), (self.x + 50, self.y + self.r)),  # /
            ((self.x, self.y + 5*self.r), (self.x - 50, self.y + 6*self.r)),  # /
            ((self.x, self.y + 5*self.r), (self.x + 50, self.y + 6*self.r))  # \
        ]

    def draw_muñeco(self, screen):
        def extremidades(pos_inicio, pos_fin):
            pygame.draw.line(screen, self.color, pos_inicio, pos_fin, 4)

        if self.contador >= 1:
            pygame.draw.circle(screen, self.color, (self.x, self.y), self.r, 4)
            for i in range(self.contador % 7 - 1):
                extremidades(self.pos_figura[i][0], self.pos_figura[i][1])
