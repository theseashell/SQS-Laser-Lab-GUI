import time
import socket

class CoboldPCTCPIP:
    def __init__(self, ipaddress, port):
        self.ipaddress = 'localhost'
        self.port = 38080

        self.DAq = 'part1.ccf'
        self.DAn = 'part2.ccf'

        self.analysis = 'ANALYSIS'
        self.comment = 'nocomment'

    def establishConnection(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print('connecting to {} port {}'.format(self.ipaddress,self.port))
        self.sock.connect((self.ipaddress,self.port))
        self.sock.settimeout(1.0)

    def disconnect(self):
        self.sock.close()
        print('Disconnected.')

    def setDAq(self):
        self.sock.sendall(('execute '+self.DAq+'\n').encode())

        try:
            print('Set DAq file.')
            self.sock.recv(1024)
        except Exception as e:
            pass    #print(e)

    def setDAn(self):
        self.sock.sendall(('execute '+self.DAn+'\n').encode())

        try:
            print('Set DAn file.')
            self.sock.recv(1024)
        except Exception as e:
            pass    #print(e)

    def setNewHardware(self,aqtime,filename):
        self.sock.sendall(f'new hardware,{filename},{self.analysis},'\
                           f'{aqtime:.0f}s,{self.comment}\n'.encode())

        try:
            print('Set Hardware.')
            self.sock.recv(1024)
        except Exception as e:
            pass    #print(e)

    def startAquisition(self):
        self.sock.send('start\n'.encode())
        try:
            print('Started aquisition.')
            self.sock.recv(1024)
        except Exception as e:
            pass    #print(e)

    def checkCoboldStatus(self):
        finished = False
        while not finished:
            self.sock.sendall('get_status\n'.encode())
            answer = self.sock.recv(1024)

            #print('Cobold Status: {}'.format(answer.decode()))
            if answer.decode().strip('\x00') == "1":
                print('Aquisition done.')
                break

            time.sleep(1.0)

    def startScan(self, aqtime, filename):
        self.setDAq()
        self.setNewHardware(float(aqtime), filename)
        self.setDAn()
        self.startAquisition()
        self.checkCoboldStatus()

"""
cobold = CoboldPCTCPIP('localhost', 38080)
cobold.establishConnection()
cobold.startScan(10, 'C:/Users/exfelsqs/Desktop/Measurements/CoboldTCPIPTest/Wurstwasser2')
cobold.disconnect()
"""