import pygame
from random import randint




class dinozavrik(pygame.sprite.Sprite):

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def __init__(self):
        super().__init__()
        self.dx = 0
        self.y_speed = 0
        self.image = pygame.image.load("dinizavrik.png")
        self.image = pygame.transform.scale(self.image, (50,50))
        # self.image = pygame.Surface((50, 50))
        # self.image.fill(pygame.Color("green"))
        self.rect = self.image.get_rect()
        self.rect.center = (50, 350)
        self.per = True
        self.kaktus = []
    def test(self):
      self.per = True

      if self.per == True:
          if self.y_speed < 0:
            self.y_speed *= 0.7
          self.rect.y += self.y_speed
          self.y_speed += 1


      if self.rect.y >= 450:
          self.rect.y = 450
          self.per = False

      qwerty = pygame.key.get_pressed()
      if qwerty[pygame.K_w] and self.rect.y >= 450:
          self.per = True
          self.y_speed = -60





