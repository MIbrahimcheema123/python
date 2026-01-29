import pygame
pygame.init()
screen = pygame.display.set_mode((500,250))
run = False
while not run:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run = True
    pygame.draw.rect(screen,pygame.Color("green"),pygame.Rect(100,100,100,100))
    pygame.display.flip()