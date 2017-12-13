import random as rnd

node = hou.pwd()
geo = node.geometry()
f= hou.frame() # necessary to evaluate every frame

r = rnd.random()
g = rnd.random() * 0.1
b = rnd.random() * 0.05
color = (r,g,b)
Cd = geo.addAttrib(hou.attribType.Point, "Cd", color)

for point in geo.points():
    oldColor = point.attribValue(Cd)
    oldR = oldColor[0]
    oldG = oldColor[1]
    oldB= oldColor[2]
    y = point.position()[1]
    random = rnd.random()
    
    newR = oldR + random * 2
    newG = y * (random * 0.55) * 2
    newB = y * (random * 0.15) * 2
    
    newColor = (newR, newG, newB)
    point.setAttribValue(Cd, newColor)


#~ ~~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ 

import _alembic_hom_extensions as abc

node = hou.pwd()
geo = node.geometry()

def println(msg):
    hou.ui.displayMessage(msg)
    
#~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~     

fileName = "untitled.abc"
filePath = "$HIP//"
url = filePath + fileName
for geo in abc.alembicGetSceneHierarchy(url, "/")[2]: 
    println(str(geo))

'''
oldAttr = abc.alembicUserProperty("Cd")
println(str(oldAttr))

r = float(oldAttr[5])
g = float(oldAttr[1])
b = float(oldAttr[2])
color = (r, g, b)
Cd = geo.addAttrib(hou.attribType.Point, "Cd", color)

for point in geo.points():
    point.setAttribValue(Cd, color)

'''


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


import _alembic_hom_extensions as abc

node = hou.pwd()
geo = node.geometry()

'''
Gets an alembic attribute from the cache
Requires an abcFileName detail attribute

@attrName: name of attribute to retrieve
@useTransform: looks on the parent node instead. Equivalent to using maya transform instead of shape
'''

def println(msg):
    hou.ui.displayMessage(msg)

fileName = "untitled.abc"
filePath = "$HIP//"
url = filePath + fileName

geoListRaw = abc.alembicGetSceneHierarchy(url, "/")[2]
geoList = []

for i in range(0, len(geoListRaw)):
    geoName = geoListRaw[i][0]
    geoList.append(geoName)
    
#println(str(geoList))

# transform
#path = path.rsplit("/", 1)[0]

'''
x =  abc.alembicArbGeometry(url, path, "Cd", 0.0)
if x[0]:
    println(x[0][0])
'''



