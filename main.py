import pygame, sys, random
from pygame.locals import *
import revolver

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

    titleFont = pygame.font.SysFont(None,72)
    title = titleFont.render("REVOLVER",True,(255,255,255))
    DISPLAYSURF.blit(title,((WIDTH/2-140),540))
    pygame.display.update()

    # Init game variables
    revolver = revolver.revolver()

    def printKeys():
        print "Keys:\n"
        print "a - pull hammer\nl - pull trigger\nr - load bullet\nt - rotate cylinder by one\nb - spin cylinder\np - DEBUG print weapon status"

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
            if event.type == pygame.KEYDOWN and event.key == pygame.K_a:
                revolver.cock()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_l:
                revolver.fire()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                revolver.load()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_p:
                revolver.printStatus()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_t:
                revolver.rotateCylinder()
                print 'Rotating cylinder by one'
            if event.type == pygame.KEYDOWN and event.key == pygame.K_b:
                revolver.spinCylinder()


            if event.type == pygame.KEYDOWN and event.key == pygame.K_h:
                printKeys()



        inputDetect = False

