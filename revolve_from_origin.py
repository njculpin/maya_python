# revolve from origin
import maya.cmds as cmds

# number of copies plus the angle of rotation
iterations = 16
angle = 22

# original geometry position
posX = 2
posY = 2
posZ = 2

def freezeit():
    cmds.select(cmds.listRelatives(cmds.ls(geometry=True), p=True, path=True), r=True)
    cmds.makeIdentity(apply=True, t=1, r=1, s=1, n=0)
    cmds.move(posX, posY, posZ, ".scalePivot",".rotatePivot", absolute=True)
    revolve(iterations)

def revolve(iterations):
    if iterations == 1:
        print ("stop")
    else:    
        cmds.select()
        cmds.duplicate()
        cmds.makeIdentity(apply=True, t=1, r=1, s=1, n=0)
        cmds.move(posX, posY, posZ, ".scalePivot",".rotatePivot", absolute=True)
        cmds.rotate(0,angle,0)
        print ("iteration = ",str(iterations))
        revolve(iterations-1)
        
freezeit()

