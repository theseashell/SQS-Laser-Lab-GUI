from PyQt5 import QtCore

from numpy import linspace
from time import sleep

##QThreadTest##
class leclaserpowerscanThread(QtCore.QThread):

    #Property to exit scan loop
    T_threadactive = QtCore.pyqtSignal(bool)

    #Connection to signal receivers
    T_lecPBval = QtCore.pyqtSignal(int)
    T_infoTextBrowser = QtCore.pyqtSignal(str)
    T_laserpowerprogressBar = QtCore.pyqtSignal(int)

    #Getting values for lec laser power scan
    T_leclpfirst = QtCore.pyqtSignal(int)
    T_leclplast = QtCore.pyqtSignal(int)
    T_leclpsteps = QtCore.pyqtSignal(int)
    T_leclpinttime = QtCore.pyqtSignal(int)

    def run(self):
        #Setting Progressbar to 0
        self.T_lecPBval.emit(0)

        #Get array of powers
        powers = linspace(self.T_leclpfirst, self.T_leclplast, self.T_leclpsteps)

        i = 1
        for p in powers:
            if self.T_threadactive:
                self.T_infoTextBrowser.emit(f'Adjusting laser power to {p} % ...')
                #Update laser power progress bar
                self.T_laserpowerprogressBar.emit(p)
                #<<-- Function to change waveplate position
                self.T_infoTextBrowser.emit('Laser power adjusted.')
                self.T_infoTextBrowser.emit(f'Started aquisition ({self.T_leclpinttime} s) of channel {self.T_oscchannel} ...')
                #<<-- Function that starts the aquisition
                sleep(self.T_leclpinttime)
                self.T_infoTextBrowser.emit(f'Finished aquisition.')
                #Update progressbar
                self.T_lecPBval.emit(i/self.T_leclpsteps*100)
                i += 1
            else:
                break

        self.T_infoTextBrowser.emit('The lec laser power scan is done.')

    def stop(self):
        self.T_threadactive = False
        self.wait()