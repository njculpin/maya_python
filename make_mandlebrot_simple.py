import maya.cmds as cmds

# number of copies plus the angle of rotation
iterations = 16
angle = 22

# original geometry position
posX = 2
posY = 2
posZ = 2

def mandel(c):
        z=0
        for h in range(0,20):
                z = z**2 + c
                if abs(z) > 2:
                        break
        if abs(z) >= 2:
                return False
        else:
                return True


def draw():
        for x in range(0,600):
                real = x / 200.0 - 1.5
                for y in range(0,600):
                        img = y / 200.0 - 1.5
                        c = complex(real, img)
                        if mandel(c):
                                print("point",str(real),str(img))
                                cmds.polyCube(h=1,w=1,d=1)
                                cmds.move(real*200,img*200,0)
                        
draw()
        
        