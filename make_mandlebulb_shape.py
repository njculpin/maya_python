# Make MandleBulb
# mandelbrot set = f(x) = x2 + c
# Nick Culpin
# 11/25/2015

import maya.cmds as cmds
from math import trunc
import random
import sys
from decimal import Decimal

# set recursion limit
sys.setrecursionlimit(1500)

#check to see if our window exists
if cmds.window('utility', exists = True):
    cmds.deleteUI('utility')
# create our window
window = cmds.window('utility', widthHeight = (200, 200), title = 'Mandlebulb', resizeToFitChildren=1, sizeable = True)
cmds.setParent(menu=True)
# create a main layout
mainLayout = cmds.rowColumnLayout(numberOfColumns=1, columnAlign=(1, 'left'), columnWidth=(2, 150) )
MakeSphere = cmds.button(label = 'Make Sphere Prim', width = 150, height = 40, c = lambda *_:makeSpherePrim())
LevelsOfFractals = cmds.intSliderGrp(l='Point Limit: ',min=1, max=1000,field=True,v=1)
RealNumber = cmds.floatSliderGrp( label='Real Number', field=True, minValue=-2.0, maxValue=2.0, fieldMinValue=-2.0, fieldMaxValue=2.0, v=0 )
ImagNumber = cmds.floatSliderGrp( label='Imaginary Number', field=True, minValue=-2.0, maxValue=2.0, fieldMinValue=-2.0, fieldMaxValue=2.0, v=0 )
MakeFractal = cmds.button(label = 'Make Fractal Shape', width = 150, height = 40, c = lambda *_:getValues())
MoveToOrign = cmds.button(label = 'Move To Origin', width = 150, height = 40, c = lambda *_:moveToOrigin())
MakeFractalChildren = cmds.button(label = 'Make Fractal Shape Children', width = 150, height = 40, c = lambda *_:freezeChildren())
LevelsOfRevolution = cmds.intSliderGrp(l='Revolution Limit: ',min=1, max=1000,field=True,v=1)
rotationDistance = cmds.floatSliderGrp( label='Rotation Angle', field=True, minValue=-360.0, maxValue=360.0, fieldMinValue=-360.0, fieldMaxValue=360, v=0 )
Revolve = cmds.button(label = 'Revolve', width = 150, height = 40, c = lambda *_:getRevolveValues())
# show window
cmds.showWindow(window)

#############################
# starting values
x = 0
y = 0
seed = 0

def makeSpherePrim():
    cmds.polySphere(sx=5, sy=5, r=20)
    
def freezeChildren():
    # freeze the children and re-run
    cmds.select(cmds.listRelatives(cmds.ls(geometry=True), p=True, path=True), r=True)
    cmds.makeIdentity(apply=True, t=1, r=1, s=1, n=0)
    getValues()
    
def moveToOrigin():
    # group and move all geo to origin
    cmds.select(cmds.listRelatives(cmds.ls(geometry=True), p=True, path=True), r=True)
    cmds.makeIdentity(apply=True, t=1, r=1, s=1, n=0)
    cmds.group(n='tempGroup')
    bbox = cmds.exactWorldBoundingBox()
    bottom = [(bbox[0] + bbox[3])/2, bbox[1], (bbox[2] + bbox[5])/2]
    cmds.xform(piv=bottom, ws=True)
    cmds.move(rpr=True)
    cmds.ungroup('tempGroup')

def getValues():
    # query the values from sliders
    i = cmds.intSliderGrp(LevelsOfFractals,q=True,v=True)
    Real = cmds.floatSliderGrp(RealNumber,q=True,v=True)
    Imag = cmds.floatSliderGrp(ImagNumber,q=True,v=True)
    return TransformMandelbrot(i,Real,Imag,seed)

def TransformMandelbrot(i,Real,Imag,seed):
    
    if i > 0:
        
        print ('Real Number = ' +str(Real))
        print ('Imaginary Number = ' +str(Imag))
        
        c = complex(Real,Imag)
        print ('c = ' +str(c))
        newC = ((seed**2) + c)
        seed = newC
        
        # if magnitude goes above 2, the point has escaped to infinite and will not draw. 
        magnitude = abs(seed)
    
        if magnitude >= 2:
            # if the point escapes to infinite, print infinite
            print ('infinite')
        else:
            # use the magnitude of the point as scale...larger number = smaller scale. 2 = scale 0. 0 = scale 1.
            print ('safe')
            scaleV = magnitude
    
            # simple multiplier to x and y so that the change is noticed
            x = newC.real * 100
            y = newC.imag * 100
            # remove decimals past the 100s place
            x = trunc(x*100)/10
            y = trunc(y*100)/10
            z = 0
    
            print ('x = ' +str(x))
            print ('y = ' +str(y))
            print ('scale = ' +str(scaleV))    
    
            # translate the point with the new x,y & scale values
            cmds.duplicate()
            cmds.move(x,y,z)
            cmds.scale(scaleV,scaleV,scaleV)
            
            return TransformMandelbrot(i-1,Real,Imag,seed)
    else:
        print ('end of line')       
        return
    
def getRevolveValues():
    # select all geometry, Unite and duplicate it
    cmds.select(cmds.listRelatives(cmds.ls(geometry=True), p=True, path=True), r=True)
    cmds.polyUnite(n='set')
    cmds.duplicate('set')    
    lor = cmds.intSliderGrp(LevelsOfRevolution,q=True,v=True)
    rot = cmds.floatSliderGrp(rotationDistance,q=True,v=True)
    revolve(lor,rot)
    
def revolve(lor,rot):
    if lor == 0:
        print ('stop')
        return 1
    else:
        cmds.select('set')
        cmds.duplicate()
        cmds.rotate(0,rot,0)
    
    return revolve(lor-1,rot+(cmds.floatSliderGrp(rotationDistance,q=True,v=True)))