from PyQt5 import QtCore

from numpy import linspace
from time import sleep

##QThreadTest##
class cpcstagepositionscanThread(QtCore.QThread):

    #Property to exit scan loop
    T_threadactive = QtCore.pyqtSignal(bool)

    #Connection to signal receivers
    T_cpcPBval = QtCore.pyqtSignal(int)
    T_infoTextBrowser = QtCore.pyqtSignal(str)

    #Getting values for cpc laser power scan
    T_cpcspfirst = QtCore.pyqtSignal(int)
    T_cpcsplast = QtCore.pyqtSignal(int)
    T_cpcspsteps = QtCore.pyqtSignal(int)
    T_cpcspinttime = QtCore.pyqtSignal(int)

    def run(self):
        #Setting Progressbar to 0
        self.T_cpcPBval.emit(0)

        #Get array of powers
        positions = linspace(self.T_cpcspfirst, self.T_cpcsplast, self.T_cpcspsteps)

        i = 1
        for p in positions:
            if self.T_threadactive:
                self.T_infoTextBrowser.emit(f'Moved stage to {p} mm ...')
                #<<-- Function to change stage position
                self.T_infoTextBrowser.emit('Stage movement done.')
                self.T_infoTextBrowser.emit(f'Started aquisition ({self.T_cpcspinttime} s) ...')
                #<<-- Function that starts the aquisition
                sleep(self.T_cpcspinttime)
                self.T_infoTextBrowser.emit(f'Finished aquisition.')
                #Update progressbar
                self.T_cpcPBval.emit(i/self.T_cpcspsteps*100)
                i += 1
            else:
                break

        self.T_infoTextBrowser.emit('The cpc stage position scan is done.')

    def stop(self):
        self.T_threadactive = False
        self.wait()