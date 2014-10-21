
import pygame, time, copy
from pygame.locals import *

pygame.init()

#Video Settings
FPS = 60
WINDOWWIDTH = 1280
WINDOWHEIGHT =  720
fpsClock = pygame.time.Clock()

#Game Initialization
DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
pygame.display.set_caption('Two Point Seven Kelvin')

#Ship class
class Ship:
    def __init__(self, name):
        self.name = name
        self.mass = mass

#background image
background = pygame.image.load('test_background.jpg')
background = pygame.transform.smoothscale(background, (WINDOWWIDTH, WINDOWHEIGHT))

#Main Loop
while True:
    DISPLAYSURF.blit(background, background.get_rect())
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()
        pygame.display.update()
        fpsClock.tick(FPS)
