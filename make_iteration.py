import maya.cmds as cmds
import sys
import random as random
              
# ITERATIONS
numberofmodels = 5
geoSource = cmds.listRelatives('GeometrySource')
objectList = []

def iterate():
    # hide the source geometry
    cmds.setAttr('GeometrySource.visibility',0)
    
    # list each piece of geometry and make a random selection from it
    for i in geoSource:
        list = cmds.listRelatives(i)
        cmds.select(random.choice(list))
        selection = cmds.ls(sl=True)
        selectionName = selection[0]
        cmds.duplicate(st=True,n='new1')
        cmds.setAttr('new1.visibility',1)
        
def count ():
    # Count the number of created objects
    length = len(geoSource)
    length = length + 1
    for g in geoSource:
        length -= 1
        objectList.append('new'+str(length))
        # stop the loop so it does not include Zero value
        if length == 1:
            return 0;
            
def merge():
    cmds.polyUnite(objectList,name='Model_1')
    cmds.delete(objectList)
    del objectList[:]
    
def slide():
    versions = numberofmodels
    distance = 0
    number = 0
    while versions != 0:
        versions -= 1
        distance += 300
        number += 1
        print 'versions remaining ' + str(versions)
        print 'distance ' + str(distance)
        cmds.select('Model_'+str(number))
        cmds.move(distance,0,0)
        iterate()
        count()
        merge()
        
iterate()
count()
merge()
slide()

