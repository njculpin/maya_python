# Random Shape Generator
# Nick Culpin
# 8/24/2015

import maya.cmds as cmds
import math
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
# Controls
cmds.text( label='Select Primatives' )
cmds.separator( style='none' )
Cube = cmds.checkBox( label='Cube' )
Sphere = cmds.checkBox( label='Sphere' )
Cylinder = cmds.checkBox( label='Cylinder' )
SoccerBall = cmds.checkBox( label='Soccer Ball' )
Pyramid = cmds.checkBox( label='Pyramid' )
Torus = cmds.checkBox( label='Torus' )
Cone = cmds.checkBox( label='Cone' )
cmds.separator( style='none' )
# Number of Primatives Slider
NumberOfPrimatives = cmds.intSliderGrp(l='Number of Primatives',min=1, max=100,field=True,v=1)
# Make Button & use the slider as a arugment
Make = cmds.button(label = 'Make Brush', width = 150, height = 40, c = lambda *_:CheckSliderValueNumberOfPrims())
cmds.separator( style='none' )
cmds.separator( style='single' )
cmds.separator( style='none' )
# show window
cmds.showWindow(window)

def CheckSliderValueNumberOfPrims():
    n = cmds.intSliderGrp(NumberOfPrimatives,q=True,v=True)
    print 'nui = ' + str(n)    
    #lambda *_:MakeShape(n)
    MakeShape(n)

def MakeShape(n):
    shapeList = MakeList()
    # Execute A Random Function From The List
    if n == 0:
        print ('n = ' + str(n) + ' equal to zero')
        print ('stopped')
        cmds.select(cmds.listRelatives(cmds.ls(geometry=True), p=True, path=True), r=True)
        cmds.polyUnite()
        cmds.delete(ch=True)
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

# Make a list of functions based on user selection    
def MakeList():
    # Empty Shape List
    shapeList = []
    # Query each check box
    CubeChecked = cmds.checkBox(Cube,q = True, v = True)
    SphereChecked = cmds.checkBox(Sphere,q = True, v = True)
    CylinderChecked = cmds.checkBox(Cylinder,q = True, v = True)
    SoccerBallChecked = cmds.checkBox(SoccerBall,q = True, v = True)
    PyramidChecked = cmds.checkBox(Pyramid,q = True, v = True)
    TorusChecked = cmds.checkBox(Torus,q = True, v = True)
    ConeChecked = cmds.checkBox(Cone,q = True, v = True)

    # if a particular check box is On, Add to Our Shape List
    if CubeChecked == True:
        print 'Cube Checked'
        shapeList.append('RandomCube')
    else:
        print 'Cube Not Checked'

    if SphereChecked == True:
        print 'Sphere Checked'
        shapeList.append('RandomSphere')
    else:
        print 'Sphere Not Checked'

    if CylinderChecked == True:
        print 'Cylinder Checked'
        shapeList.append('RandomCylinder')
    else:
        print 'Cylinder Not Checked'

    if SoccerBallChecked == True:
        print 'Soccerball Checked'
        shapeList.append('RandomSoccerBall')
    else:
        print 'Soccerball Not Checked'

    if PyramidChecked == True:
        print 'Pyramid Checked'
        shapeList.append('RandomPyramid')
    else:
        print 'Pyramid Not Checked'

    if TorusChecked == True:
        print 'Torus Checked'
        shapeList.append('RandomCube')
    else:
        print 'Torus Not Checked'

    if ConeChecked == True:
        print 'Cone Checked'
        shapeList.append('RandomCone')
    else:
        print 'Cone Not Checked'

    return shapeList     

# Random Value Generator
def RandomCube():
    cmds.polyCube( h = random.randrange(1,50), w = random.randrange(1,50), d = random.randrange(1,50), sx = 4, sy = 4 )
    cmds.select()
    Transforms()
    cmds.makeIdentity(apply=True, t=1, r=1, s=1, n=0)
    cmds.duplicate()
    cmds.scale(-1,1,1)

def RandomCylinder():
    cmds.polyCylinder(h = random.randrange(1,50), r = random.randrange(1,50), sx=4, sy=4, sz=4)
    cmds.select()
    Transforms()
    cmds.makeIdentity(apply=True, t=1, r=1, s=1, n=0)
    cmds.duplicate()
    cmds.scale(-1,1,1)

def RandomSphere():
    cmds.polySphere(r = random.randrange(1,50), sx=4, sy=4)
    cmds.select()
    Transforms()
    cmds.makeIdentity(apply=True, t=1, r=1, s=1, n=0)
    cmds.duplicate()
    cmds.scale(-1,1,1)

def RandomSoccerBall():
    cmds.polyPrimitive( r=random.randrange(1,50), l=random.randrange(1,50), pt=0)
    cmds.select()
    Transforms()
    cmds.makeIdentity(apply=True, t=1, r=1, s=1, n=0)
    cmds.duplicate()
    cmds.scale(-1,1,1)

def RandomPyramid():    
    cmds.polyPyramid(ns = random.randrange(1,50), w = random.randrange(1,50), sh = 4, sc = 4 )
    cmds.select()
    Transforms()
    cmds.makeIdentity(apply=True, t=1, r=1, s=1, n=0)
    cmds.duplicate()
    cmds.scale(-1,1,1)

def RandomCone():
    cmds.polyCone( r = random.randrange(1,50),h = random.randrange(1,50), sx=4, sy=4, sz=4)
    cmds.select()
    Transforms()
    cmds.makeIdentity(apply=True, t=1, r=1, s=1, n=0)
    cmds.duplicate()
    cmds.scale(-1,1,1)

def RandomTorus():
    cmds.polyTorus(sx=4, sy=4, r=random.randrange(1,50), sr=random.randrange(1,50))
    cmds.select()
    Transforms()
    cmds.makeIdentity(apply=True, t=1, r=1, s=1, n=0)
    cmds.duplicate()
    cmds.scale(-1,1,1)

# Transforms for each shape are randomized
def Transforms():    
    cmds.scale(random.randrange(1,10),random.randrange(1,10),random.randrange(1,10))
    cmds.rotate(random.randrange(1,355),random.randrange(1,355),random.randrange(1,355))
    cmds.move(0,random.randrange(-5,5),random.randrange(-2,2))

