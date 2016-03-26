#Imports:
from Tactix.window.initialize import initWindow
from Tactix.game.tank import Tank
from Tactix.input.arrows import arrowWeight
from pygame.locals import *
import pygame
import time
import math
import sys

#initWindow starts pygame, opens a window, and returns a drawing surface.
screen = initWindow("Tactix Engine Test",(1000,700))
#This number controls the speed at which the tank moves.
speed = 1/6
#This creates a new tank object.
#The first 2 arguements specify the base and turret sprites so you can mix and match tanks and turrets.
#The third arguement specifies the starting position of the tank, and the forth, the starting size.
tank = Tank("Resources/Sprites/GreenTankBase.png","Resources/Sprites/GreenTankTurret.png",(200,200),(100,100))

#This function handles the directional weight of the arrow keys.
#This function moves the tank and rotates the chasis accordingly.
def handleDirectional(d):
    if d[0] == 1:
        tank.setPos((tank.getPos()[0]+speed,tank.getPos()[1]))
        tank.setDir(90)
    if d[0] == -1:
        tank.setPos((tank.getPos()[0]-speed,tank.getPos()[1]))
        tank.setDir(90)
    if d[1] == 1:
        tank.setPos((tank.getPos()[0],tank.getPos()[1]+speed))
        tank.setDir(0)
    if d[1] == -1:
        tank.setPos((tank.getPos()[0],tank.getPos()[1]-speed))
        tank.setDir(0)
    if d == [1,1] or d == [-1,-1]:
        tank.setDir(45)
    if d == [1,-1] or d == [-1,1]:
        tank.setDir(135)

#This function calculates the angle at which to rotate the turret.
#It uses pygame to find the current mouse position and points the turret there.
def updateAim():
    tx,ty = pygame.mouse.get_pos()
    x,y = tank.getPos()
    tank.setRot(-math.degrees(math.atan2(ty-y,tx-x))-90)

#This is the main game loop
#This loop clears the screen, updates the tank position and angle, then redraws
#the tank on the screen. It also handles quit events so that the program closes
#when the red X is pressed on the window.
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    handleDirectional(arrowWeight())
    updateAim()
    screen.fill((255,255,255))
    tank.draw(screen)
    pygame.display.flip()
