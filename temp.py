import _alembic_hom_extensions as abc

def getAbcAttr(attrName):
    """
    Gets an alembic attribute from the cache
    Requires an 'abcFileName' detail attribute
    
    @attrName: name of attribute to retrieve
    @useTransform: looks on the parent node instead. Equivalent to using maya's transform instead of shape
    """
    
    geo = hou.pwd().geometry()
    time = hou.frame() / hou.fps()
    
    if geo.findGlobalAttrib("abcFileName") is not None:
        url = geo.attribValue("abcFileName")

        for childGeo in abc.alembicGetSceneHierarchy(url, "/")[2]:  
            path = "/" + childGeo[0] + "/" + childGeo[2][0][0]
            
            x = abc.alembicArbGeometry(url, path, attrName, time)
            print(x) 
            
getAbcAttr("Cd")

#~ ~~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ 

import _alembic_hom_extensions as abc

def println(msg):
    hou.ui.displayMessage(str(msg))

def getAbcAttr(attrName, useTransform=False):
    """
    Gets an alembic attribute from the cache
    Requires an 'abcFileName' detail attribute
    
    @attrName: name of attribute to retrieve
    @useTransform: looks on the parent node instead. Equivalent to using maya's transform instead of shape
    """
    geo = hou.pwd().curPrim().geometry()
    if geo.findGlobalAttrib("abcFileName") is not None:
        abcPath = geo.attribValue("abcFileName")
        
        path = hou.pwd().curPrim().attribValue("path")
        if useTransform:
            path = path.rsplit("/", 1)[0]
        
        x =  abc.alembicArbGeometry(abcPath, path, attrName, hou.frame() / hou.fps())
        if x[0]:
            return x[0][0]
        else:
            return ''

return getAbcAttr('myAttrname', useTransform=True)

#~ ~~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ 

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
    hou.ui.displayMessage(str(msg))
    
#~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~     

for geo in abc.alembicGetSceneHierarchy(url, "/")[2]: 

    println(abc.alembicUserProperty(url, geo[0], "Cd", 0))

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



