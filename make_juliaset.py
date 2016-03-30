# Random Maya Julia Set
import random
import maya.cmds as cmds

def JuliaSet():
    
    xa = -2.0
    xb = 1.0
    ya = -1.5
    yb = 1.5
    
    maxIt = 32
    imgx = 256
    imgy = 256
    
    c = complex(random.random() * 2.0 - 1.0, random.random() - 0.5)
    
    for y in range(imgy):
        zy = y * (yb - ya) / (imgy - 1)  + ya
        for x in range(imgx):
            zx = x * (xb - xa) / (imgx - 1) + xa
            z = complex(zx, zy)
            for i in range(maxIt):
                if abs(z) > 2.0: break 
                z = z * z + c 
            r = i % 4 * 64
            g = i % 8 * 32
            b = i % 16 * 16
            
            xAxis = x
            yAxis = y
            zAxis = 0
            scale = r/255.0
            
            if r >= 0.94117647058:
                print("infinite")
                if r <= 0.1:
                    print ("infinite")
                else:
                    print ("cube printed")
                    print ("at location = ",str(xAxis),str(yAxis),str(zAxis))
                    print ("scaled = ",str(scale))
                    cmds.polyCube()
                    cmds.move(xAxis,yAxis,zAxis)
                    cmds.scale(scale,scale,scale)             
   
JuliaSet()
