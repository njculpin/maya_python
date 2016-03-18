# Make Fractal Random
# Nick Culpin
# 11/25/2015

import maya.cmds as cmds
import random


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
    
TransformFractalRandom(5)



