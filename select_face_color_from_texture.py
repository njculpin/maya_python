'''
This is a work in progress...the script reads the texture file for a piece of selected geometry
after it has been imported into maya. The user is then asked to select a color which exsists
inside of the texture. The script then goes through each face and selects it, if the face contains
more than 50% of the chosen color.

'''
import maya.cmds as cmds

textureName = ['file1']
geometryName = ['model']

#color pick
rPick = 0.0
gPick = 0.0
bPick = 0.0

def main():
    rgb = pickColor()
    uvList = getUV()
    faceList = getFaces()

    # null starting values should be left at 1
    coordCount = 1

    # selct the geometry & get the number of coords to check
    cmds.select(geometryName[0])
    coords = cmds.polyEvaluate(uv=True)


    selectedUVs  = []
    compareUVs = []
    picked = []
    
    # for each UV coordinate found
    for uv in uvList:

        # define inital values for selected color from color picker
        r = 0.0
        b = 0.0
        g = 0.0

        # define rgb values from each uv coord
        rPick = rgb[0]
        gPick = rgb[1]
        bPick = rgb[2]        

        # if the coord count is NOT equal to the total number of coords to check...keep checking
        if coordCount != coords:

            # get the float rgb values for each color coord
            rSample = cmds.colorAtPoint(str(textureName[0]), o='RGB',u=uv[0], v=uv[1])[0]
            gSample = cmds.colorAtPoint(str(textureName[0]), o='RGB',u=uv[0], v=uv[1])[1]
            bSample = cmds.colorAtPoint(str(textureName[0]), o='RGB',u=uv[0], v=uv[1])[2]

            # round values and convert to 0 to 255
            rPoint = round(rSample * 255)
            gPoint = round(gSample * 255)
            bPoint = round(bSample * 255)

            # print the coord that is currently being checked

            # subtract the coord from the total coords to get the remaining
            coordRemain = int(coords) - 1            

            # compare coord color to picked color
            if rPoint == rPick and gPoint == gPick and bPoint == bPick:
                # if the color matches, add the uv coord to the list of selected
                # if the coord color value matches the picked value, add the coorffd to the selected uv list
                selectedUVs.append(uv)

            # if the coord count is not yet equal to the total number of coords, continue processing coords
            if coordCount != coords:
                # add 1 to the total completed
                coordCount += 1
                # print the percentage remaining
                complete = float(coordCount) / float(coords) * float(100)
                remaining = float(100)-complete
                rounded = round(remaining)

                if rounded < 1:
                    print ('finishing')
                else:
                    print (str(rounded) +'% remaining')

            # if the coordCount becomes equal to the number of coords, compare each list
            if coordCount == coords:
                # get the bounding box for the list of all the faces in geometry
                for bounds in faceList[0]:
                    xFace = bounds[0]
                    yFace = bounds[1]                        
                    xFaceMin = xFace[0]
                    xFaceMax = xFace[1]
                    yFaceMin = yFace[0]
                    yFaceMax = yFace[1]                  
                    
                    # we have a list of uvs with the color selected
                    for youvee in selectedUVs:
                        # now we need to compare each colored uv location with the face bounding boxes.
                        if xFaceMin <= youvee[0] <= xFaceMax and yFaceMin <= youvee[1] <= yFaceMax:
                                compareUVs.append(youvee)
                                
                # we lost the name of the face when comparing the matched uv with the bounds of the face.
                # we get the matched uv list and recheck it against the face bounds and then select the face.
                for i in compareUVs:
                    xUV = i[0]
                    yUV = i[1]                                       
                
                    for face in faceList[1]:
                        cmds.select(face)
                        boundsCheck = cmds.polyEvaluate(bc2=True)
                        xFace = boundsCheck[0]
                        yFace = boundsCheck[1]                        
                        xFaceMin = xFace[0]
                        xFaceMax = xFace[1]
                        yFaceMin = yFace[0]
                        yFaceMax = yFace[1]
                        
                        if xFaceMin <= xUV <= xFaceMax and yFaceMin <= yUV <= yFaceMax:
                            # if the UV bounds falls inside of the Facebounds, append the face to the picked list
                            picked.append(face)
                            
            # print the picked list, and select each face inside of it.
            print 'picked = ' + str(picked)
            for p in picked:
                cmds.polyCut(p)
                              
# select a color via UI and change the Pick RGB values
def pickColor():
    # open color picker
    result = cmds.colorEditor()
    buffer = result.split()
    # if done picking a color, get the colors values
    if '1' == buffer[3]:
        values = cmds.colorEditor(query=True, rgb=True)
        # picked colors become markRGB plus rounded markup
        rFloat = values[0]
        gFloat = values[1]
        bFloat = values[2]

        rPick = round(rFloat * 255)
        gPick = round(gFloat * 255)
        bPick = round(bFloat * 255)

        return rPick, gPick, bPick
    else:
        print 'Editor was dismissed'

def getUV():
    # collection of uv coordinates
    cmds.select(geometryName)
    count = cmds.polyEvaluate(uv=True)
    listUVCount = range(1,count)
    c = 1
    uvList = []

    for i in listUVCount:
        while c != count:
            c += 1
            cmds.select(str(geometryName[0])+'.map['+str(c)+']')
            positions = cmds.polyEditUV(q=True)
            uvList.append(positions)
            if c == count:
                return uvList

def getFaces():
    # count faces
    faceCount = cmds.polyEvaluate(geometryName[0],f=True)
    # make a list of face count
    faceRange = list(range(1,faceCount))

    # empty list for face
    faceList = []

    # for each face in faceRange, get the name of the face
    for f in faceRange:
        # get the name of each face on the model
        face = (str(geometryName[0])+'.f['+str(f)+']')

        # append each face to the faceList
        faceList.append(face)

    faceCount = cmds.polyEvaluate(geometryName[0],f=True)

    # empty list for facebounds
    fb = []

    # if the faceList is equal to the number of faces found    
    if len(faceList) == faceCount-1:
        # for each face name found in face list
        for face in faceList:
            # select each face
            cmds.select(face)
            # get the UV bounding box on each face
            faceBounds = cmds.polyEvaluate(bc2=True)
            # print the facebounds
            fb.append(faceBounds)

    if len(fb) == len(faceList):
        return fb,faceList

main()