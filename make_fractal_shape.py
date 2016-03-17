# Make Fractal
# Nick Culpin
# 11/25/2015

import maya.cmds as cmds
import math
from math import trunc
import random
import sys
from decimal import Decimal


#check to see if our window exists
if cmds.window('utility', exists = True):
    cmds.deleteUI('utility')
# create our window
window = cmds.window('utility', widthHeight = (200, 200), title = 'Make-A-Shape', resizeToFitChildren=1, sizeable = True)
cmds.setParent(menu=True)
# create a main layout
mainLayout = cmds.rowColumnLayout(numberOfColumns=1, columnAlign=(1, 'left'), columnWidth=(2, 150) )
# Variation Selection
FractalCollection = cmds.radioCollection()
RandomVariation = cmds.radioButton(label="Random")
TreeVariation = cmds.radioButton(label="Tree")
LevelsOfFractals = cmds.intSliderGrp(l='Point Limit: ',min=1, max=40,field=True,v=1)
MakeFractal = cmds.button(label = 'Make Fractal Shape', width = 150, height = 40, c = lambda *_:CheckFractalRadioButtons())
# show window
cmds.showWindow(window)


def CheckFractalRadioButtons():
    RandomChecked = cmds.radioButton(RandomVariation,q = True,select=True)
    TreeChecked = cmds.radioButton(TreeVariation,q = True,select=True)

    if RandomChecked == True:
        print 'random checked'
        i = cmds.intSliderGrp(LevelsOfFractals,q=True,v=True)  
        cmds.select(cmds.listRelatives(cmds.ls(geometry=True), p=True, path=True), r=True)
        TransformFractalRandom(i)        
    else:
        print 'random not checked'

    if TreeChecked == True:
        print 'Mandelbrot checked'
        i = cmds.intSliderGrp(LevelsOfFractals,q=True,v=True)  
        cmds.select(cmds.listRelatives(cmds.ls(geometry=True), p=True, path=True), r=True)
        TransformFractalTree(i)        
    else:
        print 'random not checked'  

def TransformFractalRandom(i):
    if i <= 0:
        print ('i = ' + str(i) + ' equal to zero')
        print ('stopped')   
        return 1
    else:
        print ('i = ' + str(i))
        cmds.makeIdentity(apply=True, t=1, r=1, s=1, n=0)
        cmds.duplicate()
        cmds.rotate(random.randrange(1,355),random.randrange(1,355),random.randrange(1,355))
        cmds.move(random.randrange(-200,200),random.randrange(-200,200),random.randrange(-200,200))        
        return TransformFractalRandom(i - 1)

def TransformFractalTree(i):
    if i <= 0:
        print ('i = ' + str(i) + ' equal to zero')
        print ('stopped')   
        return 1
    else:
        print ('i = ' + str(i))
        cmds.select(cmds.listRelatives(cmds.ls(geometry=True), p=True, path=True), r=True)
        cmds.makeIdentity(apply=True, t=1, r=1, s=1, n=0)
        cmds.delete(ch=True)
        # Make the Fractal
        cmds.duplicate()
        cmds.rotate(random.randrange(0,180),random.randrange(0,180),random.randrange(0,180))
        cmds.move(random.randrange(0,150),random.randrange(2,100),random.randrange(0,150))
        cmds.scale(.7,.7,.7)

        return TransformFractalTree(i - 1) 


