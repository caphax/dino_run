import pygame


class obstical(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = None
        self.rect = None

    def move(self):
        self.rect.x -= 10
        if self.rect.x <= -50:
            self.kill()
            return 1
        return 0



    # def draw(self, screen):
    #     screen.blit(self.image, self.rect)
    #     print(1)

    def update(self):
        return self.move()

