import pygame, sys, random
from pygame.locals import *

if __name__ == "__main__":
    
    # Initialisation
    pygame.init()
    WIDTH = 800
    HEIGHT = 600
    DISPLAYSURF = pygame.display.set_mode((WIDTH,HEIGHT))
    pygame.display.set_caption("Revolver")
    backroundColor = 212,150,150
    cBLACK = 45,45,45
    splash = pygame.image.load("revolver.jpg")
    splashrect = splash.get_rect()
    DISPLAYSURF.blit(splash,splashrect)
    pygame.display.update()

    inputDetect = False
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                inputDetect = True
                pygame.quit()
                sys.exit()

