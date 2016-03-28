#MakeShape
import maya.cmds as cmds
import math
import random
import sys
from decimal import Decimal

shapeList = ['RandomCube','RandomCylinder','RandomSphere','RandomSoccerBall','RandomPyramid','RandomCone','RandomTorus']
created = []

# note that n*2 because of mirror function...2 == 4 objects
n = 3

def MakeShape(n):

    # Execute A Random Function From The List
    if n == 0:
        print ('n = ' + str(n) + ' equal to zero')
        print ('stopped')
        return 1
    else:
        print ('n = ' + str(n))
        ShapeName = random.choice(shapeList)
        print (ShapeName)
        possibles = globals().copy()
        possibles.update(locals())
        method = possibles.get(ShapeName)
        if not method:
            raise Exception("Method %s not implemented" % ShapeName)
        method()        
        return MakeShape(int(n) - 1)  
        
# Random Value Generator ; each function creates a primative with random attributes, then mirrors it. 
# it will also add each newly created object to created list for merging
def RandomCube():
    cmds.polyCube( h = random.randrange(1,50), w = random.randrange(1,50), d = random.randrange(1,50), sx = 4, sy = 4 )
    cmds.select()
    Transforms()
    cmds.makeIdentity(apply=True, t=1, r=1, s=1, n=0)
    created.append(cmds.ls(selection=True))
    
    cmds.duplicate()
    cmds.scale(-1,1,1)
    created.append(cmds.ls(selection=True))

def RandomCylinder():
    cmds.polyCylinder(h = random.randrange(1,50), r = random.randrange(1,50), sx=4, sy=4, sz=4)
    cmds.select()
    Transforms()
    cmds.makeIdentity(apply=True, t=1, r=1, s=1, n=0)
    created.append(cmds.ls(selection=True))
    
    cmds.duplicate()
    cmds.scale(-1,1,1)
    created.append(cmds.ls(selection=True))

def RandomSphere():
    cmds.polySphere(r = random.randrange(1,50), sx=4, sy=4)
    cmds.select()
    Transforms()
    cmds.makeIdentity(apply=True, t=1, r=1, s=1, n=0)
    created.append(cmds.ls(selection=True))
    
    cmds.duplicate()
    cmds.scale(-1,1,1)
    created.append(cmds.ls(selection=True))

def RandomSoccerBall():
    cmds.polyPrimitive( r=random.randrange(1,50), l=random.randrange(1,50), pt=0)
    cmds.select()
    Transforms()
    cmds.makeIdentity(apply=True, t=1, r=1, s=1, n=0)
    created.append(cmds.ls(selection=True))
    
    cmds.duplicate()
    cmds.scale(-1,1,1)
    created.append(cmds.ls(selection=True))

def RandomPyramid():    
    cmds.polyPyramid(ns = random.randrange(1,50), w = random.randrange(1,50), sh = 4, sc = 4 )
    cmds.select()
    Transforms()
    cmds.makeIdentity(apply=True, t=1, r=1, s=1, n=0)
    created.append(cmds.ls(selection=True))
    
    cmds.duplicate()
    cmds.scale(-1,1,1)
    created.append(cmds.ls(selection=True))

def RandomCone():
    cmds.polyCone( r = random.randrange(1,50),h = random.randrange(1,50), sx=4, sy=4, sz=4)
    cmds.select()
    Transforms()
    cmds.makeIdentity(apply=True, t=1, r=1, s=1, n=0)
    created.append(cmds.ls(selection=True))
    
    cmds.duplicate()
    cmds.scale(-1,1,1)
    created.append(cmds.ls(selection=True))

def RandomTorus():
    cmds.polyTorus(sx=4, sy=4, r=random.randrange(1,50), sr=random.randrange(1,50))
    cmds.select()
    Transforms()
    cmds.makeIdentity(apply=True, t=1, r=1, s=1, n=0)
    created.append(cmds.ls(selection=True))

    cmds.duplicate()
    cmds.scale(-1,1,1)
    created.append(cmds.ls())

# Transforms for each shape are randomized
def Transforms():    
    cmds.scale(random.randrange(1,10),random.randrange(1,10),random.randrange(1,10))
    cmds.rotate(random.randrange(1,355),random.randrange(1,355),random.randrange(1,355))
    cmds.move(0,random.randrange(-5,5),random.randrange(-2,2))
    
def merge():
    print ('created items='+str(created))
    for i in created:
        cmds.ls(str(i))
        #cmds.polyUnite( str(i), n='result' )
    
MakeShape(n)
merge()