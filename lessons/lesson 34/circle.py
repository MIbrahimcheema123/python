import pygame
pygame.init()
screen = pygame.display.set_mode((500,500))
screen.fill(pygame.Color("green"))
YELLOW = pygame.Color("yellow")
pygame.draw.circle(screen,YELLOW,(300,300),50)
pygame.draw.circle(screen,YELLOW,(100,100),50,3)
pygame.display.update()
running = True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running  = False
pygame.quit()