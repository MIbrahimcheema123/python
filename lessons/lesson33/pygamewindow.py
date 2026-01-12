import pygame
pygame.init()
screen = pygame.display.set_mode((600,700))
notdone = False
while not notdone:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    pygame.display.flip()