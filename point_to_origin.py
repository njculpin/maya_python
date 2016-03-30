import math
import maya.cmds as cmds
    
# define a target at origin for cube rotation
def make_origin_target():
    o = cmds.polySphere() # create a sphere
    cmds.select(o) # select the sphere
    bbox = cmds.exactWorldBoundingBox() # create bounding box around it
    bottom = [(bbox[0] + bbox[3])/2, bbox[1], (bbox[2] + bbox[5])/2] # define the bottom of the bounding box
    cmds.xform(piv=bottom, ws=True) # move the sphere to the bottom of the bounding box
    cmds.move(rpr=True)
    cmds.makeIdentity(apply=True, t=1, r=1, s=1, n=0) # freeze transforms

# point all geometry to the origin
def point_to_target():
    make_origin_target()
    
    cmds.select(cmds.listRelatives(cmds.ls(geometry=True), p=True, path=True), r=True)
    shapeList = cmds.ls(sl=True)
    shapeList.remove('pSphere1')
    
    for x in shapeList:
        print (x)
        cmds.select(x)
        cmds.xform(cp=True)
        cmds.aimConstraint('pSphere1',str(x))
    
point_to_target()
