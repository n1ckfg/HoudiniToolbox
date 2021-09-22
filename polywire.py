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

def openFileDialog():
    return hou.ui.selectFile(start_directory=None, title=None, collapse_sequences=False, file_type=hou.fileType.Any, pattern="*.latk, *.json", default_value=None, multiple_select=False, image_chooser=False, chooser_mode=hou.fileChooserMode.Read)

url = "/Users/nick/Desktop/flower.json"
with open(url) as data_file:
    data = json.load(data_file)

for layer in data["grease_pencil"][0]["layers"]:
    for i, frame in enumerate(layer["frames"]):
        if (i == hou.frame()):
            for stroke in frame["strokes"]:
                poly = geo.createPolygon()
                poly.setIsClosed(0)

                for point in stroke["points"]:
                    co = point["co"]
                    point = geo.createPoint()
                    point.setPosition(hou.Vector3(co[0], co[1], co[2]))
                    poly.addVertex(point);

#~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ 

node = hou.pwd()
geo = node.geometry()

pt0 = geo.createPoint()
pt0.setPosition(hou.Vector3(1, 0, 0))
pt1 = geo.createPoint()
pt1.setPosition(hou.Vector3(0, 1, 0))
pt2 = geo.createPoint()
pt2.setPosition(hou.Vector3(0, 0, 1))

poly = geo.createPolygon()
poly.setIsClosed(0)
poly.addVertex(pt0);
poly.addVertex(pt1);
poly.addVertex(pt2);