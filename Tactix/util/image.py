import pygame

def getImgSz(path):
    return (pygame.image.load(path).get_rect().size)
