# Make Fractal Tree
# Nick Culpin
# 11/25/2015

import maya.cmds as cmds
import random
  
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
    
    
TransformFractalTree(5)


