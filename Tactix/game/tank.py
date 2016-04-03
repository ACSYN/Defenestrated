from Tactix.game.entity import Entity
import math
import pygame

def turretPos(basePos,mOffset,tOffset,angle):
    mountPos = (basePos[0]+mOffset[0],basePos[1]+mOffset[1])
    hyp = math.hypot(tOffset[0],tOffset[1])
    return (round(hyp*math.cos(math.radians(angle+90))+mountPos[0])
           ,round(-hyp*math.sin(math.radians(angle+90))+mountPos[1]))

def mountPos(basePos,mOffset,angle):
    hyp = math.hypot(mOffset[0],mOffset[1])
    return (round(hyp*math.cos(math.radians(angle+90)))
           ,round(-hyp*math.sin(math.radians(angle+90))))

def scalingFactor(initSz,finalSz):
    return (finalSz[0]/initSz[0],finalSz[1]/initSz[1])

class Tank:
    def __init__(self,baseTex,turretTex,initPos,tankSz,mountOffset=(0,0),turretOffset=(0,0),initTurret=0,initDir=0):
        turretSz = (round(tankSz[0]*0.8),tankSz[1])
        self.baseTexSz = pygame.image.load(baseTex).get_rect().size
        self.turretTexSz = pygame.image.load(turretTex).get_rect().size
        baseScl = scalingFactor(self.baseTexSz,tankSz)
        turretScl = scalingFactor(self.turretTexSz,turretSz)
        self.mOffset = (mountOffset[0]*baseScl[0],mountOffset[1]*baseScl[1])
        self.tOffset = (turretOffset[0]*turretScl[0],turretOffset[1]*turretScl[1])
        self.base = Entity(baseTex,initPos,tankSz,initDir)
        self.turret = Entity(turretTex,turretPos(initPos,self.mOffset,self.tOffset,initTurret),turretSz,initTurret)
    def setPos(self,newPos):
        self.base.setPos(newPos)
        self.turret.setPos(turretPos(self.base.pos,self.mOffset,self.tOffset,self.turret.rot))
    def getPos(self):
        return self.base.pos
    def getTurretPos(self):
        return (self.base.pos[0]+self.mOffset[0],self.base.pos[1]+self.mOffset[1])
    def setDir(self,newDir):
        self.base.setRot(newDir)
        self.mOffset = mountPos(self.base.pos,self.mOffset,self.base.rot)
    def setRot(self,newAngle):
        self.turret.setRot(newAngle)
        self.turret.setPos(turretPos(self.base.pos,self.mOffset,self.tOffset,newAngle))
    def draw(self,surface):
        self.base.draw(surface)
        self.turret.draw(surface)
