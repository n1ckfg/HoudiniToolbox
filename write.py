import json
from numpy import interp

node = hou.pwd()
   
parm_url = node.parm("url").eval()
parm_armed = node.parm("armed").eval()

frameRange = hou.playbar.frameRange()
firstFrame = int(frameRange.x())
lastFrame = int(frameRange.y())
numFrames = lastFrame - firstFrame

inputs = node.inputs()
geo = inputs[0].geometry()

if (parm_armed == True):      
    FINAL_LAYER_LIST = [] # string array

    #for layer in self.layers:
    for g in range(0, 1):
        sb = [] # string array
        sbHeader = [] # string array
        sbHeader.append("\t\t\t\t\t\"frames\": [")
        sb.append("\n".join(sbHeader))

        #for h, frame in enumerate(layer.frames):
        for h in range(firstFrame, lastFrame):
            hou.setFrame(h)
            sbbHeader = [] # string array
            sbbHeader.append("\t\t\t\t\t\t{")
            sbbHeader.append("\t\t\t\t\t\t\t\"strokes\": [")
            sb.append("\n".join(sbbHeader))
            
            for i, stroke in enumerate(geo.prims()):
                sbb = [] # string array
                sbb.append("\t\t\t\t\t\t\t\t{")
                color = (0.0, 0.0, 0.0, 1.0)
                fill_color = (0.0, 0.0, 0.0, 0.0)
                
                '''
                try:
                    color = stroke.color
                    if (len(color) < 4):
                        color = (color[0], color[1], color[2], 1.0)
                except:
                    pass
                try:
                    fill_color = stroke.fill_color
                    if (len(fill_color) < 4):
                        fill_color = (fill_color[0], fill_color[1], fill_color[2], 0.0)
                except:
                    pass
                '''
                sbb.append("\t\t\t\t\t\t\t\t\t\"color\": [" + str(color[0]) + ", " + str(color[1]) + ", " + str(color[2]) + ", " + str(color[3]) + "],")
                sbb.append("\t\t\t\t\t\t\t\t\t\"fill_color\": [" + str(fill_color[0]) + ", " + str(fill_color[1]) + ", " + str(fill_color[2]) + ", " + str(fill_color[3]) + "],")

                if (len(stroke.points()) > 0): 
                    sbb.append("\t\t\t\t\t\t\t\t\t\"points\": [")
                    for j, point in enumerate(stroke.points()):
                        x = point.position().x() #point.co[0]
                        y = point.position().y() #None
                        z = point.position().z() #None
                        '''
                        r = point.vertex_color[0]
                        g = point.vertex_color[1]
                        b = point.vertex_color[2]
                        a = point.vertex_color[3]
                        if (yUp == True):
                            y = point.co[2]
                            z = point.co[1]
                        else:
                            y = point.co[1]
                            z = point.co[2]  
                        #~
                        if (useScaleAndOffset == True):
                            x = (x * globalScale[0]) + globalOffset[0]
                            y = (y * globalScale[1]) + globalOffset[1]
                            z = (z * globalScale[2]) + globalOffset[2]
                        '''
                        #~ 
                        pointStr = "\t\t\t\t\t\t\t\t\t\t{\"co\": [" + str(x) + ", " + str(y) + ", " + str(z) + "]}"#, \"pressure\": " + str(float32(point.pressure)) + ", \"strength\": " + str(float32(point.strength)) + ", \"vertex_color\": [" + str(float32(r)) + ", " + str(float32(g)) + ", " + str(float32(b)) + ", " + str(float32(a)) + "]}"
                                      
                        if (j == len(stroke.points()) - 1):
                            sbb.append(pointStr)
                            sbb.append("\t\t\t\t\t\t\t\t\t]")
                        else:
                            pointStr += ","
                            sbb.append(pointStr)
                else:
                    sbb.append("\t\t\t\t\t\t\t\t\t\"points\": []")
                
                if (i == len(geo.prims()) - 1):
                    sbb.append("\t\t\t\t\t\t\t\t}")
                else:
                    sbb.append("\t\t\t\t\t\t\t\t},")
                
                sb.append("\n".join(sbb))
            
            sbFooter = []
            #if (h == len(layer.frames) - 1): 
            if (h == lastFrame - 1): 
                sbFooter.append("\t\t\t\t\t\t\t]")
                sbFooter.append("\t\t\t\t\t\t}")
            else:
                sbFooter.append("\t\t\t\t\t\t\t]")
                sbFooter.append("\t\t\t\t\t\t},")
            sb.append("\n".join(sbFooter))
        
        FINAL_LAYER_LIST.append("\n".join(sb))
    
    s = [] # string
    s.append("{")
    s.append("\t\"creator\": \"Houdini\",")
    s.append("\t\"version\": 2.8,")
    s.append("\t\"grease_pencil\": [")
    s.append("\t\t{")
    s.append("\t\t\t\"layers\": [")

    '''
    for i, layer in enumerate(self.layers):
        s.append("\t\t\t\t{")
        if (layer.name != None and layer.name != ""): 
            s.append("\t\t\t\t\t\"name\": \"" + layer.name + "\",")
        else:
            s.append("\t\t\t\t\t\"name\": \"layer" + str(i + 1) + "\",")
            
        s.append(FINAL_LAYER_LIST[i])

        s.append("\t\t\t\t\t]")
        if (i < len(self.layers) - 1): 
            s.append("\t\t\t\t},")
        else:
            s.append("\t\t\t\t}")
            s.append("\t\t\t]") # end layers
    s.append("\t\t}")
    s.append("\t]")
    s.append("}")
    '''

    s.append("\t\t\t\t{")
    s.append("\t\t\t\t\t\"name\": \"layer0\",")
        
    s.append(FINAL_LAYER_LIST[0])

    s.append("\t\t\t\t\t]")
    s.append("\t\t\t\t}")
    s.append("\t\t\t]") # end layers
    s.append("\t\t}")
    s.append("\t]")
    s.append("}")

    with open(parm_url, "w") as f:
        f.write("\n".join(s))
        f.closed
    parm_armed = False
    node.parm("armed").set(parm_armed)

