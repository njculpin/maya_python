import math
import maya.cmds as cmds

rot = 137.5
limit = 200

# define a target at origin for cube rotation
def make_origin_target():
    o = cmds.polySphere()
    cmds.select(o)
    bbox = cmds.exactWorldBoundingBox()
    bottom = [(bbox[0] + bbox[3])/2, bbox[1], (bbox[2] + bbox[5])/2]
    cmds.xform(piv=bottom, ws=True)
    cmds.move(rpr=True)
    cmds.makeIdentity(apply=True, t=1, r=1, s=1, n=0)
    
make_origin_target()
    
def fib_seq():
    a, b = 0, 1
    while b < limit:
        a, b = b, a+b
        cube = cmds.polyCube()
        cmds.move(b,b/2,0)
        cmds.move(cube[0]+".scalePivot",cube[0]+".rotatePivot", absolute=True)
        cmds.select(cmds.listRelatives(cmds.ls(geometry=True), p=True, path=True), r=True)
        cmds.makeIdentity(apply=True, t=1, r=1, s=1, n=0)    
        cmds.rotate(0,rot,0)

fib_seq()

def point_to_target():
    cmds.select(cmds.listRelatives(cmds.ls(geometry=True), p=True, path=True), r=True)
    shapeList = cmds.ls(sl=True)
    shapeList.remove('pSphere1')
    for x in shapeList:
        print x
        cmds.aimConstraint('pSphere1',str(x))
        
point_to_target()
