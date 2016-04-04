from Tactix.game.entity import Entity
from Tactix.util.image import getImgSz
from Tactix.game.projectile import Projectile
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

#Make the scale arguement floatable. Round when setting sizes.
class Tank:
    def __init__(self,baseTex,turretTex,projectTex,impactTex,initPos,scaling,mountOffset=(0,0),turretOffset=(0,0),initTurret=0,initDir=0):
        self.baseTexSz = getImgSz(baseTex)
        self.turretTexSz = getImgSz(turretTex)
        self.projectTex = projectTex
        self.impactTex = impactTex
        self.scaling = scaling
        self.tankSz = (round(self.baseTexSz[0]*scaling),round(self.baseTexSz[1]*scaling))
        self.turretSz = (round(self.tankSz[0]*0.8),self.tankSz[1]) #Ew, more magic...
        self.turretScl = scalingFactor(self.turretTexSz,self.turretSz)
        self.mOffset = (mountOffset[0]*scaling,mountOffset[1]*scaling)
        self.tOffset = (turretOffset[0]*self.turretScl[0],turretOffset[1]*self.turretScl[1])
        self.base = Entity(baseTex,initPos,self.tankSz,initDir)
        self.turret = Entity(turretTex,turretPos(initPos,self.mOffset,self.tOffset,initTurret),self.turretSz,initTurret)
        self.projectiles = []
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
    def fire(self,target):
        hyp = math.hypot(self.tOffset[0],self.tOffset[1]) + (self.turretSz[1]/2)
        spawnPos = (hyp*math.cos(math.radians(self.turret.rot+90))+self.getTurretPos()[0]
                   ,-hyp*math.sin(math.radians(self.turret.rot+90))+self.getTurretPos()[1])
        self.projectiles.append(Projectile(self.projectTex,self.impactTex,self.turretScl[0]/4.2,spawnPos,target,1000)) #Yucky! It's ma-ma-ma-magic!
    def draw(self,surface):
        for projectile in self.projectiles:
            projectile.update()
            projectile.draw(surface)
        self.base.draw(surface)
        self.turret.draw(surface)
