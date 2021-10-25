import json
from numpy import interp

def alert(msg):
    hou.ui.displayMessage(str(msg))

def remap(value, min1, max1, min2, max2):
    return interp(value,[min1, max1],[min2, max2])

def remapInt(value, min1, max1, min2, max2):
    return int(interp(value,[min1, max1],[min2, max2]))

def openFileDialog():
    return hou.ui.selectFile(start_directory=None, title=None, collapse_sequences=False, file_type=hou.fileType.Any, pattern="*.latk, *.json", default_value=None, multiple_select=False, image_chooser=False, chooser_mode=hou.fileChooserMode.Read)
