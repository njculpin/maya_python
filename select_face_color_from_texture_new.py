#select_face_color_from_texture ; clean

import maya.cmds as cmds

# get the name of the selected model
model_name = cmds.ls(sl=1)[0].rpartition(':')[2]

# get the name of the texture on the model
texture_name = cmds.ls(str(model_name)[0].rpartition(':')[2],tex=True)

def get_faces():
    # count faces
    faceCount = cmds.polyEvaluate(model_name,f=True)
    # make a list of face count
    faceRange = list(range(1,faceCount))

    # empty list for face
    faceList = []

    # for each face in faceRange, get the name of the face
    for f in faceRange:
        # get the name of each face on the model
        face = (str(model_name)+'.f['+str(f)+']')

        # append each face to the faceList
        faceList.append(face)

    faceCount = cmds.polyEvaluate(model_name,f=True)

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
        print ("fb = ", str(fb))
        print ("facelist = ", str(faceList))
        return fb,faceList
    
get_faces()

