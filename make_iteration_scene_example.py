# SAMPLE SCENE SET UP. the following is a sample scene structure to use make_iteration.py. It creates 3 groups
# of geometry and randomly offsets them. The script then places all of the groups within a super group called
# GeometrySource. make_iteration.py requires the super group GeometrySource.

GeoCategories = ['head','left_leg','right_leg','left_arm','right_arm','leftArm']
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
        
def moverandom():
    for g in GeoCategories:
        cmds.select(str(g))
        cmds.move(random.randrange(-5,5),random.randrange(0,10),0)
        cmds.makeIdentity(apply=True, t=1, r=1, s=1, n=0)
        cmds.parent(str(g),'GeometrySource')
        #cmds.group(str(g),parent='GeometrySource')
        
make_demo_primatives()
moverandom()