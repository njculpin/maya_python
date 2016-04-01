import maya.cmds as cmds

dist = 150
rot = 137.5

def toySpiral():
    x = 0
    y = 0
    z = 0    
    
    while z < dist:
        x += 1*2
        y -= 1*1
        z += 1*.5
        print (x,y,z)
        
        cube = cmds.polyCone(h=50,r=50) # make a new brush cube
        cmds.move(x,y,z) #cut the sequence scale
        cmds.move(cube[0]+".scalePivot",cube[0]+".rotatePivot", absolute=True)# move pivit to origin
    
        cmds.select(cmds.listRelatives(cmds.ls(geometry=True), p=True, path=True), r=True) # select all geometry
        cmds.makeIdentity(apply=True, t=1, r=1, s=1, n=0) # freeze transforms    
        cmds.rotate(0,rot,0) # rotate all    
    
toySpiral()

    
    