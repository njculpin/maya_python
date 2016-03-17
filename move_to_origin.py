import maya.cmds as cmds

def fix ():
    geoSource = cmds.ls(selection=True)
    for g in geoSource:
        print 'category name = ' + str(g)
        geometry = cmds.listRelatives(g)
        for i in geometry:
            print 'found = ' + str(i)
            cmds.select(i)
            # bounding box & center each object
            bbox = cmds.exactWorldBoundingBox()
            bottom = [(bbox[0] + bbox[3])/2, bbox[1], (bbox[2] + bbox[5])/2]
            cmds.xform(piv=bottom, ws=True)
            cmds.move(rpr=True)
            # freeze transforms
            cmds.makeIdentity(apply=True, t=1, r=1, s=1, n=0)
fix()
