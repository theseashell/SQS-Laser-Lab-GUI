#Attenuator module
# How to make this script usable:
# 1. Download ximc 2.10.5 from http://files.xisupport.com/Software.en.html (Standa)
# 2. Extract everything from the folder. Copy everything the 'win64' (if you use win64)
#    folder contains to the folder where this script is located. Good luck!

import numpy as np
import sys

#if sys.version_info >= (3,0):
#    import urllib.parse

from simple_movement import *

class AttenuatorStandaTCPIP:
    def __init__(self):
        self.ipaddress = 'xi-net://192.168.140.146/'
        self.axis = '00002922'
        self.libpath = b'C:/Users/exfelsqs/PycharmProjects/Attenuator/keyfile.sqlite'

    def connectToAxis(self):
        try:
            print(self.libpath)
            sbuf = create_string_buffer(64)
            lib.ximc_version(sbuf)
            print("Library version: " + sbuf.raw.decode().rstrip("\0"))
            lib.set_bindy_key(self.libpath)
            open_name = bytes(self.ipaddress+self.axis, encoding = 'utf-8')
            print(self.ipaddress+self.axis)
            self.ID = lib.open_device(open_name)
            print(self.ID)
            print('Connection established.')
        except:
            print('Connection is not possible.')

    def closeConnection(self):
        try:
            lib.close_device(byref(cast(self.ID, POINTER(c_int))))
            print('Connection closed.')
        except:
            print('Connection could not be closed.')

    def getPosition(self):
        return get_position(lib, self.ID)

    def moveToPosition(self, position):
        lib.command_move(self.ID, int(position))
        lib.command_wait_for_stop(self.ID, 100)

    def powerToMotorPosition(self, power):
        x0 = 1879.10626848
        a = 3784.25313476
        b = 0.000695305864442
        c = 3786.71545349
        landa = 2*np.pi/b
        return 1/b*np.arcsin((-power*7540./100+c)/a)+x0-10.5*landa #7567.6 would be exact value


"""
attenuator = AttenuatorStandaTCPIP()

attenuator.connectToAxis()
print(attenuator.getPosition())

percentpower = float(sys.argv[1])
print("New target position: " + str(attenuator.powerToMotorPosition(percentpower)))
newPosition = attenuator.powerToMotorPosition(percentpower)
attenuator.moveToPosition(newPosition)
print(attenuator.getPosition())

attenuator.closeConnection()
"""