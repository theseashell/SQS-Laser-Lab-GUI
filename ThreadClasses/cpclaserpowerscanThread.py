from PyQt5 import QtCore

from numpy import linspace
from time import sleep

##QThreadTest##
class cpclaserpowerscanThread(QtCore.QThread):

    #Property to exit scan loop
    T_threadactive = QtCore.pyqtSignal(bool)

    #Connection to signal receivers
    T_cpcPBval = QtCore.pyqtSignal(int)
    T_infoTextBrowser = QtCore.pyqtSignal(str)
    T_laserpowerprogressBar = QtCore.pyqtSignal(int)


    #Getting values for cpc laser power scan
    T_cpclpfirst = QtCore.pyqtSignal(int)
    T_cpclplast = QtCore.pyqtSignal(int)
    T_cpclpsteps = QtCore.pyqtSignal(int)
    T_cpclpinttime = QtCore.pyqtSignal(int)

    def run(self):
        #Setting Progressbar to 0
        self.T_cpcPBval.emit(0)

        #Get array of powers
        powers = linspace(self.T_cpclpfirst, self.T_cpclplast, self.T_cpclpsteps)

        i = 1
        for p in powers:
            if self.T_threadactive:
                self.T_infoTextBrowser.emit(f'Adjusting laser power to {p} % ...')
                #Update laser power progress bar
                self.T_laserpowerprogressBar.emit(int(p))
                #<<-- Function to change waveplate position
                self.T_infoTextBrowser.emit('Laser power adjusted.')
                self.T_infoTextBrowser.emit(f'Started aquisition ({self.T_cpclpinttime} s) ...')
                #<<-- Function that starts the aquisition
                sleep(self.T_cpclpinttime)
                self.T_infoTextBrowser.emit(f'Finished aquisition.')
                #Update progressbar
                self.T_cpcPBval.emit(i/self.T_cpclpsteps*100)
                i += 1
            else:
                break

        self.T_infoTextBrowser.emit('The cpc laser power scan is done.')

    def stop(self):
        self.T_threadactive = False
        self.wait()