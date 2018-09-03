import json
from numpy import interp

node = hou.pwd()
geo = node.geometry()
time = hou.frame() / hou.fps()

def alert(msg):
    hou.ui.displayMessage(str(msg))

def remap(value, min1, max1, min2, max2):
    return interp(value,[min1, max1],[min2, max2])

def remapInt(value, min1, max1, min2, max2):
    return int(interp(value,[min1, max1],[min2, max2]))

url = "C:/Users/nick/Desktop/flower_testbed/flower.json"
with open(url) as data_file:
    data = json.load(data_file)

vol_res = 500
vol_geo = geo.createVolume(vol_res, vol_res, vol_res)

allX = []
allY = []
allZ = []
for layer in data["grease_pencil"][0]["layers"]:
    for frame in layer["frames"]:
        for stroke in frame["strokes"]:
            for point in stroke["points"]:
                coord = point["co"]
                allX.append(coord[0])
                allY.append(coord[1])
                allZ.append(coord[2])
allX.sort()
allY.sort()
allZ.sort()

for layer in data["grease_pencil"][0]["layers"]:
    for i, frame in enumerate(layer["frames"]):
    	if (i == hou.frame()):
	        for stroke in frame["strokes"]:
	            for point in stroke["points"]:
	                coord = point["co"]
	                x = remapInt(coord[0], allX[0], allX[len(allX)-1], 0, vol_res-1);
	                y = remapInt(coord[1], allY[0], allY[len(allY)-1], 0, vol_res-1);
	                z = remapInt(coord[2], allZ[0], allZ[len(allZ)-1], 0, vol_res-1);
	                vol_geo.setVoxel((x, y, z), 100.0)

#~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ 

import json
from numpy import interp

node = hou.pwd()
geo = node.geometry()
time = hou.frame() / hou.fps()

def alert(msg):
    hou.ui.displayMessage(str(msg))

def remap(value, min1, max1, min2, max2):
    return interp(value,[min1, max1],[min2, max2])

def remapInt(value, min1, max1, min2, max2):
    return int(interp(value,[min1, max1],[min2, max2]))

url = "C:/Users/nick/Desktop/flower_testbed/flower.json"
with open(url) as data_file:
    data = json.load(data_file)

vol_res = 500
vol_geo = geo.createVolume(vol_res, vol_res, vol_res)

allX = []
allY = []
allZ = []
for layer in data["grease_pencil"][0]["layers"]:
    for frame in layer["frames"]:
        for stroke in frame["strokes"]:
            for point in stroke["points"]:
                coord = point["co"]
                allX.append(coord[0])
                allY.append(coord[1])
                allZ.append(coord[2])
allX.sort()
allY.sort()
allZ.sort()

layers = []
for layer in data["grease_pencil"][0]["layers"]:
    frames = []
    for frame in layer["frames"]:
        strokes = []
        for stroke in frame["strokes"]:
            points = []
            for point in stroke["points"]:
                coord = point["co"]
                x = remapInt(coord[0], allX[0], allX[len(allX)-1], 0, vol_res-1);
                y = remapInt(coord[1], allY[0], allY[len(allY)-1], 0, vol_res-1);
                z = remapInt(coord[2], allZ[0], allZ[len(allZ)-1], 0, vol_res-1);
                points.append((x,y,z))
            strokes.append(points)
        frames.append(strokes)
    layers.append(frames)

for layer in layers:
    for i, frame in enumerate(layer):
        if (i == hou.frame()):
            for stroke in frame:
                for point in stroke:
                    vol_geo.setVoxel((point[0], point[1], point[2]), 100.0)

#~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ 

import json
from numpy import interp

node = hou.pwd()
geo = node.geometry()

def alert(msg):
    hou.ui.displayMessage(str(msg))

def remap(value, min1, max1, min2, max2):
    return interp(value,[min1, max1],[min2, max2])

def remapInt(value, min1, max1, min2, max2):
    return int(interp(value,[min1, max1],[min2, max2]))

url = "C:/Users/nick/Desktop/flower_testbed/flower.json"
with open(url) as data_file:
    data = json.load(data_file)

vol_res = 500
vol_geo = geo.createVolume(vol_res, vol_res, vol_res)

allX = []
allY = []
allZ = []
for layer in data["grease_pencil"][0]["layers"]:
    for frame in layer["frames"]:
        for stroke in frame["strokes"]:
            for point in stroke["points"]:
                coord = point["co"]
                allX.append(coord[0])
                allY.append(coord[1])
                allZ.append(coord[2])
allX.sort()
allY.sort()
allZ.sort()

for layer in data["grease_pencil"][0]["layers"]:
    for frame in layer["frames"]:
        for stroke in frame["strokes"]:
            for point in stroke["points"]:
                coord = point["co"]
                x = remapInt(coord[0], allX[0], allX[len(allX)-1], 0, vol_res-1);
                y = remapInt(coord[1], allY[0], allY[len(allY)-1], 0, vol_res-1);
                z = remapInt(coord[2], allZ[0], allZ[len(allZ)-1], 0, vol_res-1);
                vol_geo.setVoxel((x,y,z), 100.0)

#~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ 

node = hou.pwd()
geo = node.geometry()

vol_res = 100
vol_geo = geo.createVolume(vol_res, vol_res, vol_res)

voxelData = [] # float

for i in range(0, vol_res * vol_res * vol_res):
    voxelData.append(0.000001 * i)

vol_geo.setAllVoxels(voxelData)

for i in range(0, vol_res):
    vol_geo.setVoxel((i,i,i), 100.0)