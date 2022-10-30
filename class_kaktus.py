import pygame
from class_obstract_opstical import obstical

class short_kaktus(obstical):

    def __init__(self):
        super().__init__()
        # self.image = pygame.image.load('cactus.png')
        # self.image = pygame.transform.scale(self.image, (40, 50))

        self.image = pygame.Surface((40, 30))
        self.image.fill(pygame.Color('white'))
        self.rect = self.image.get_rect()
        self.rect.x = 900
        self.rect.y = 470

    def draw_coligion(self, screen):
        pygame.draw.rect(screen, pygame.Color('red'), (self.rect), 2)


class long_kaktus(obstical):

    def __init__(self):
        super().__init__()
        # self.image = pygame.image.load('cactus.png')
        # self.image = pygame.transform.scale(self.image, (40, 50))

        self.image = pygame.Surface((40, 90))
        self.image.fill(pygame.Color('white'))
        self.rect = self.image.get_rect()
        self.rect.x = 900
        self.rect.y = 410

    def draw_coligion(self, screen):
        pygame.draw.rect(screen, pygame.Color('red'), (self.rect), 2)


