import sys
sys.path.extend(['/usr/local/Cellar/python3/3.2.2/lib/python3.2/site-packages/distribute-0.6.24-py3.2.egg','/usr/local/Cellar/python3/3.2.2/lib/python32.zip','/usr/local/Cellar/python3/3.2.2/lib/python3.2','/usr/local/Cellar/python3/3.2.2/lib/python3.2/plat-darwin','/usr/local/Cellar/python3/3.2.2/lib/python3.2/lib-dynload','/usr/local/Cellar/python3/3.2.2/lib/python3.2/site-packages'])
import serial
deviceID = '/dev/tty.usbmodemfd121'
ser = serial.Serial(deviceID, 9600)

import bpy

from bge import logic
from bge import events

def Player():

    cont = logic.getCurrentController()
    obj = cont.owner
    #print(dir(obj))
    
    #motion = cont.actuators['Motion']
    print("Hello")
    
    line = ser.readline().strip()
    line = str( line, encoding='utf8' )
    vals = line.split(',')
    vals = [int(i) for i in vals if i!='']
    if len(vals) == 11:
        if vals[0] == 0:
            #print(dir(motion))
            #motion.dLoc = [0.0, vals[1]/10, 0.0]
            obj.localPosition.y = vals[1]
            #cont.activate(motion)
            print(line)
    
    #cube = bpy.data.objects["Cube"]

    
def Rangefinder():
    cont = logic.getCurrentController()
    obj = cont.owner
    line = ser.readline().strip()
    line = int(str( line, encoding='utf8' ))
    print(line)
    obj.localPosition.y = line


