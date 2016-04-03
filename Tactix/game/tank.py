from Tactix.game.entity import Entity
import math
import pygame

def turretPos(basePos,mOffset,offset,angle):
    mountPos = (basePos[0]+mOffset[0],basePos[1]+mOffset[1])
    return (round(offset[1]*math.cos(math.radians(angle+90))+mountPos[0])
           ,round(-offset[1]*math.sin(math.radians(angle+90))+mountPos[1]))

def mountPos(basePos,mOffset,angle):
    hyp = math.hypot(mOffset[0],mOffset[1])
    return (round(hyp*math.cos(math.radians(angle+90)))
           ,round(-hyp*math.sin(math.radians(angle+90))))

class Tank:
    def __init__(self,baseTex,turretTex,initPos,tankSz,mountOffset=(0,0),turretOffset=0,initTurret=0,initDir=0):
        self.base = Entity(baseTex,initPos,tankSz,initDir)
        self.mOffset = mountOffset
        self.tOffset = turretOffset
        turretSz = (round(tankSz[0]*0.8),tankSz[1])
        self.turret = Entity(turretTex,turretPos(initPos,self.mOffset,self.tOffset,initTurret),turretSz,initTurret)
    def setPos(self,newPos):
        self.base.setPos(newPos)
        self.turret.setPos(turretPos(self.base.pos,self.mOffset,self.tOffset,self.turret.rot))
    def getPos(self):
        return self.base.pos
    def setDir(self,newDir):
        self.base.setRot(newDir)
        self.mOffset = mountPos(self.base.pos,self.mOffset,self.base.rot)
    def setRot(self,newAngle):
        self.turret.setRot(newAngle)
        self.turret.setPos(turretPos(self.base.pos,self.mOffset,self.tOffset,newAngle))
    def draw(self,surface):
        self.base.draw(surface)
        self.turret.draw(surface)
