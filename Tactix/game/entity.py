import pygame

class Entity(pygame.sprite.Sprite):
    def __init__(self,initTex,initPos,scaledSz=None,initRot=0):
        self.grp = pygame.sprite.Group()
        self.tex = pygame.image.load(initTex).convert_alpha()
        self.pos = initPos
        self.rot = initRot
        pygame.sprite.Sprite.__init__(self,self.grp)
        if scaledSz:
            self.tex = pygame.transform.scale(self.tex,scaledSz)
        self.image = pygame.transform.rotate(self.tex,self.rot)
        self.rect = self.image.get_rect()
        self.rect.center = self.pos
    def setPos(self,newPos):
        self.pos = newPos
        self.rect.center = self.pos
    def setRot(self,newRot):
        self.rot = newRot
        self.image = pygame.transform.rotate(self.tex,self.rot)
        self.rect = self.image.get_rect()
        self.rect.center = self.pos
    def draw(self,surface):
        self.grp.draw(surface)
