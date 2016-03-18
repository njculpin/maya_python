# SAMPLE SCENE SET UP. the following is a sample scene structure to use make_iteration.py. It creates 3 groups
# of geometry and randomly offsets them. The script then places all of the groups within a super group called
# GeometrySource. make_iteration.py requires the super group GeometrySource.

GeoCategories = ['head','left_leg','right_leg','left_arm','right_arm','torso']
shapes = ['cube','cylinder','sphere','ball','pyramid','cone','torus']
cmds.group( em=True, name='GeometrySource' )

def make_demo_primatives():
    for g in GeoCategories:
        cube = cmds.polyCube(name=str(g)+'_cube',sx = 4, sy = 4)
        cylinder = cmds.polyCylinder(name=str(g)+'_cylinder',sx=4, sy=4, sz=4)
        sphere = cmds.polySphere(name=str(g)+'_sphere',sx=4, sy=4)
        ball = cmds.polyPrimitive(name=str(g)+'_ball',pt=0)
        pyramid = cmds.polyPyramid(name=str(g)+'_pyramid',sh = 4, sc = 4)
        cone = cmds.polyCone(name=str(g)+'_cone',)
        torus = cmds.polyTorus(name=str(g)+'_torus',sx=4, sy=4)
        cmds.group( cube,cylinder,sphere,ball,pyramid,cone,torus, n=str(g))

        
def transforms():
    for g in GeoCategories:
        
        if g == 'head':
            for s in shapes:
                cmds.select(str(g)+'_'+str(s))
                cmds.move(0,100,0)
                cmds.scale(20,20,20)
                cmds.makeIdentity(apply=True, t=1, r=1, s=1, n=0)
                
        if g == 'left_leg':
            for s in shapes:
                cmds.select(str(g)+'_'+str(s))
                cmds.move(-50,0,0)
                cmds.scale(20,20,20)
                cmds.makeIdentity(apply=True, t=1, r=1, s=1, n=0)
                
        if g == 'right_leg':
            for s in shapes:
                cmds.select(str(g)+'_'+str(s))
                cmds.move(50,0,0)
                cmds.scale(20,20,20)
                cmds.makeIdentity(apply=True, t=1, r=1, s=1, n=0)
                
        if g == 'left_arm':
            for s in shapes:
                cmds.select(str(g)+'_'+str(s))
                cmds.move(-50,75,0)
                cmds.scale(20,20,20)
                cmds.makeIdentity(apply=True, t=1, r=1, s=1, n=0)
        
        if g == 'right_arm':
            for s in shapes:
                cmds.select(str(g)+'_'+str(s))
                cmds.move(50,75,0)
                cmds.scale(20,20,20)
                cmds.makeIdentity(apply=True, t=1, r=1, s=1, n=0)
                
        if g == 'torso':
            for s in shapes:
                cmds.select(str(g)+'_'+str(s))
                cmds.move(0,75,0)
                cmds.scale(20,20,20)
                cmds.makeIdentity(apply=True, t=1, r=1, s=1, n=0)  

        cmds.parent(str(g),'GeometrySource')
        
make_demo_primatives()
transforms()