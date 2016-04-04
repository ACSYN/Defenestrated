import pygame
from Tactix.util.image import getImgSz
from Tactix.game.entity import Entity
import math

class Projectile:
    def __init__(self,proTex,impactTex,scaling,spawnPos,targetPos,velocity,impDuration=100):
        self.impactTex = impactTex
        self.proTexSz = getImgSz(proTex)
        self.impTexSz = getImgSz(impactTex)
        self.projectileSz = (round(self.proTexSz[0]*scaling),round(self.proTexSz[1]*scaling))
        self.impactSz = (round(self.impTexSz[0]*scaling*2),round(self.impTexSz[1]*scaling*2)) #Yuck, magic numbers!
        self.iTex = impactTex
        self.target = targetPos
        self.vel = velocity
        self.impDur = impDuration
        self.clock = pygame.time.Clock()
        #May need to adjust this angle by 90 degrees
        self.angle = -math.degrees(math.atan2(targetPos[1]-spawnPos[1],targetPos[0]-spawnPos[0]))
        self.bullet = Entity(proTex,spawnPos,self.projectileSz,self.angle-90)
        self.impact = None
    def update(self):
        self.clock.tick()
        realVel = self.vel * (self.clock.get_time() / 1000) #Dividing by 1000 converts the ms to s.
        if math.hypot(self.target[0]-self.bullet.pos[0],self.target[1]-self.bullet.pos[1]) > realVel:
            newX = realVel*math.cos(math.radians(self.angle))+self.bullet.pos[0]
            newY = -realVel*math.sin(math.radians(self.angle))+self.bullet.pos[1]
            self.bullet.setPos((newX,newY))
        elif not self.impact:
            self.bullet.kill()
            self.impact = Entity(self.impactTex,self.target,self.impactSz,self.angle-90)
        elif self.impDur > 0:
            self.impDur -= self.clock.get_time()
        else:
            self.impact.kill()
    def draw(self,surface):
        self.bullet.draw(surface)
        if self.impact:
            self.impact.draw(surface)
