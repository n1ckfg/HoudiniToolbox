import json
from numpy import interp

node = hou.pwd()
geo = node.geometry()
time = hou.frame() / hou.fps()

def cacheJson(url):
    data = None
    if "jsonLoaded" in hou.expressionGlobals():
        data = hou.expressionGlobals()["jsonLoaded"];
    else:
        with open(url) as data_file:
            data = json.load(data_file)
        hou.expressionGlobals()['jsonLoaded'] = data
    return data

parm_url = node.parm("url").eval()
data = cacheJson(parm_url)

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

