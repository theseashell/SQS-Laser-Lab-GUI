from PyQt5 import QtCore

from numpy import linspace
from time import sleep

##QThreadTest##
class lecstagepositionscanThread(QtCore.QThread):

    #Property to exit scan loop
    T_threadactive = QtCore.pyqtSignal(bool)

    #Connection to signal receivers
    T_lecPBval = QtCore.pyqtSignal(int)
    T_infoTextBrowser = QtCore.pyqtSignal(str)

    #Getting values for lec laser power scan
    T_lecspfirst = QtCore.pyqtSignal(int)
    T_lecsplast = QtCore.pyqtSignal(int)
    T_lecspsteps = QtCore.pyqtSignal(int)
    T_lecspinttime = QtCore.pyqtSignal(int)

    def run(self):
        #Setting Progressbar to 0
        self.T_lecPBval.emit(0)

        #Get array of powers
        powers = linspace(self.T_lecspfirst, self.T_lecsplast, self.T_lecspsteps)

        i = 1
        for p in powers:
            if self.T_threadactive:
                self.T_infoTextBrowser.emit(f'Moved stage to {p} mm ...')
                #<<-- Function to change waveplate position
                self.T_infoTextBrowser.emit('Stage movement done.')
                self.T_infoTextBrowser.emit(f'Started aquisition ({self.T_lecspinttime} s) of channel {self.T_oscchannel} ...')
                #<<-- Function that starts the aquisition
                sleep(self.T_lecspinttime)
                self.T_infoTextBrowser.emit(f'Finished aquisition.')
                #Update progressbar
                self.T_lecPBval.emit(i/self.T_lecspsteps*100)
                i += 1
            else:
                break

        self.T_infoTextBrowser.emit('The lec laser power scan is done.')

    def stop(self):
        self.T_threadactive = False
        self.wait()