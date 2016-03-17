# create a simple 16 frame turn table scene using a placeholder object group
# user will place model within placeholder Model Group and render

angle = 0
time = 1

def placeholder_object():
    cmds.polyCube(n='placeholder')
    cmds.group('placeholder',n='Model')
    cmds.move(0,5,0)
    cmds.select('placeholder')
    cmds.CenterPivot('placeholder')
    # set initial 0 frame   
    key_frames(angle, time)

def key_frames(angle,time):
    cmds.rotate( 0, angle, 0, 'Model' )
    cmds.setKeyframe('Model',t=time)
    
    if time <= 16:
        return key_frames(angle+22.5,time+1)
    
def scene_create():
    key_frames(angle,time)
    
    cmds.directionalLight(n='key',intensity=.4,rs=True)
    cmds.rotate(-45,-45,0)
    cmds.scale(10,10,10)
    cmds.setAttr("keyShape.lightAngle",5)
    cmds.setAttr("keyShape.shadowRays",15)
    cam = cmds.camera(n='maincamera')
    cmds.move(0,4.5,12)

    cmds.group('maincamera1','key', n='Scene')
    cmds.group('Scene','Model',n='ALL')
    
placeholder_object()
scene_create()