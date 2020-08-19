import vxi11
import numpy as np
import matplotlib.pyplot as plt
from struct import unpack

class LeCroyWavePro:
    def __init__(self):
        self.address = 'TCPIP::10.254.8.38::INSTR'

    def establishConnection(self):
        try:
            self.scope = vxi11.Instrument(self.address)
            print(self.scope.ask('*IDN?'))
        except:
            print('Connection not established.')

    def setDataTransferParams(self):
        self.scope.write("CMFT DEF9,WORD,BIN")

    def recordTrace(self, channel):
        # get V axis
        gainVert = self.scope.ask("F{:d}:INSPECT? VERTICAL_GAIN".format(channel))
        gainVert = float(gainVert.split()[3])
        offsetVert = self.scope.ask("F{}:INSPECT? VERTICAL_OFFSET".format(channel))
        offsetVert = float(offsetVert.split()[3])

        dump = self.scope.write("F{:d}:WF? DAT1".format(channel))
        waveform = self.scope.read_raw()
        dbyte = int(len(waveform))
        trace = np.array(unpack('%sb' % dbyte, waveform))
        vtrace = gainVert * trace - offsetVert

        # get t axis
        intervHorz = self.scope.ask("F{}:INSPECT? HORIZ_INTERVAL".format(channel))
        intervHorz = float(intervHorz.split()[3])
        trigdelay = self.scope.ask("F1:TRIG_DELAY?")
        trigdelay = float(trigdelay.split()[1])
        ttrace = (np.array(range(len(vtrace))) - len(vtrace)//2) * intervHorz - trigdelay

        return ttrace, vtrace

"""
scope = LeCroyWavePro()
scope.establishConnection()
scope.setDataTransferParams()
time, voltage = scope.recordTrace(1)

plt.figure()
plt.plot(time*1e6,voltage,".")
plt.show()
"""