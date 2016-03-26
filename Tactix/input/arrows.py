import pygame
from pygame.locals import *

def arrowWeight():
    directional = [0,0]
    if pygame.key.get_pressed()[K_UP]:
        directional[1] += -1
    if pygame.key.get_pressed()[K_DOWN]:
        directional[1] += 1
    if pygame.key.get_pressed()[K_LEFT]:
        directional[0] += -1
    if pygame.key.get_pressed()[K_RIGHT]:
        directional[0] += 1
    return directional
