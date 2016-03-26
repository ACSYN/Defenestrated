from Tactix.game.entity import Entity
import math
import pygame

def turretPos(basePos,offset,angle):
    return (round(offset*math.cos(math.radians(angle+90))+basePos[0]),
            round(-offset*math.sin(math.radians(angle+90))+basePos[1]))

class Tank:
    def __init__(self,baseTex,turretTex,initPos,tankSz,initTurret=0,initDir=0):
        self.base = Entity(baseTex,initPos,tankSz,initDir)
        self.offset = (0.25*tankSz[1])
        turretSz = (round(tankSz[0]*0.5),tankSz[1])
        self.turret = Entity(turretTex,turretPos(initPos,self.offset,initTurret),turretSz,initTurret)
    def setPos(self,newPos):
        self.base.setPos(newPos)
        self.turret.setPos(turretPos(self.base.pos,self.offset,self.turret.rot))
    def getPos(self):
        return self.base.pos
    def setDir(self,newDir):
        self.base.setRot(newDir)
    def setRot(self,newAngle):
        self.turret.setRot(newAngle)
        self.turret.setPos(turretPos(self.base.pos,self.offset,newAngle))
    def draw(self,surface):
        self.base.draw(surface)
        self.turret.draw(surface)
