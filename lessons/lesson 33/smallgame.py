import pygame
pygame.init()
SCREEN_WIDTH,SCREEN_HEIGHT = 500,500
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("GAME")
bg_image = pygame.transform.scale(pygame.image.load("python/lessons/lesson33/bg.png").convert(),(SCREEN_WIDTH,SCREEN_HEIGHT))
p_image = pygame.transform.scale(pygame.image.load("python/lessons/lesson33/pen.png").convert_alpha(),(200,200))
penguin_rect = p_image.get_rect(center = (SCREEN_WIDTH//2,SCREEN_HEIGHT//2 - 30))
text = pygame.font.Font(None,36).render("HELLO WORLD",True,pygame.Color("black"))
text_rect =text.get_rect(center = (SCREEN_WIDTH//2,SCREEN_HEIGHT//2 + 110))
def game_loop():
    clock = pygame.time.Clock()
    notdone = False
    while not notdone:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                notdone = True
        screen.blit(bg_image,(0,0))
        screen.blit(p_image,penguin_rect)
        screen.blit(text,text_rect)
        pygame.display.flip()
        clock.tick(30)
    pygame.quit()
if __name__ == "__main__":
    game_loop()