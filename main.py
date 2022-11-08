from random import randint
import pygame
from class_plaer import dinozavrik
from class_kaktus import long_kaktus, short_kaktus
from saport import colide
from class_obstract_opstical import obstical

def close_game():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
kaktuses = pygame.sprite.Group()
RES = 800
fps = 60
chet = 0


pygame.init()
screen = pygame.display.set_mode((RES, RES))
clock = pygame.time.Clock()

dino = dinozavrik()
t = pygame.time.get_ticks()
shrift = pygame.font.Font(None, 120)


while True:
#    print(chet)
    collide = pygame.Rect.collidelist(dino.rect, kaktuses.sprites())

    screen.fill('black')


    if len(kaktuses) < 3 and pygame.time.get_ticks() - t >= randint(400, 9000):
        t = pygame.time.get_ticks()
        if randint(1,3) == 1:
            kaktuses.add(long_kaktus())
        else:
            kaktuses.add(short_kaktus())

    dino.test()

    # print(dino.rect)
    # print(kaktuses.sprites())
    # print(short_kaktus)
    # print(long_kaktus)


    for i in kaktuses:
        chet += i.update()


    kaktuses.draw(screen)

    # print(dino.rect, long_kaktus().rect)
    # print(short_kaktus().rect)


    screen.blit(shrift.render(f'chet {chet}', True, (100,150,0)), (30, 20))

    for i in kaktuses:


        i.draw_coligion(screen)
        if colide(dino.rect, i.rect):
            if collide == 0:
                while True:
                    screen.fill('black')
                    screen.blit(shrift.render('GAME OVER', True, (200,0,0)), (140, 100))
                    screen.blit(shrift.render('click in spase', True, (50,0,0)), (140, 170))
                    pygame.display.update()
                    close_game()
                    if pygame.key.get_pressed()[pygame.K_SPACE]:
                        kaktuses = pygame.sprite.Group()
                        chet = 0
                        break


    pygame.draw.rect(screen, pygame.Color('white'), (0, 500, 900, 5))
    dino.draw(screen)
    dino.draw_coligion(screen)




    clock.tick(fps)
    pygame.display.update()
    close_game()

