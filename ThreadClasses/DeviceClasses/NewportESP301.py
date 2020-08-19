import socket
import time
import sys

class newportESP301:
    def __init__(self, ipaddress, port, axis):
        self.ipaddress = ipaddress  # here 192.168.140.200
        self.port = port            # 10001
        self.axis = str(int(axis))
        self.cmt = '\r'
        self.connected = False
        self.ismoving = False
        self.smalleststep = 0.05 # µm light travels twice the distance, c=0.3µm/fs,
                                 # -> tmin = 0.1µm/0.3µm/fs = 0.33 fs
        self.timezeroPosition = 0.0

    def establishConnection(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print('Connecting to {} port {}'.format(self.ipaddress, self.port))
        self.sock.connect((self.ipaddress, self.port))
        self.connected = True
        print('Connection established.')

    def closeConnection(self):
        if self.connected == True:
            self.sock.close()
        self.connected = False
        print('Disconnected.')

    def getReply(self):
        reply = b""
        CRLF = False
        while CRLF == False:
            answer = self.sock.recv(1024)
            reply += answer
            if reply[-2:] == b"\r\n":
                CRLF = True
        return reply[:-2]
        
    def axisMotionStatus(self, printt = True):
        self.sock.sendall((self.axis+'MD?\r').encode())
        answer = int(self.getReply().decode())
        if printt:
            print('Motion Status: {} (0 = moving, 1 = stopped)'.format(answer))
        return answer

    def axisPosition(self, printt = True):
        self.sock.sendall((self.axis+'TP?\r').encode())
        answer = float(self.getReply().decode())
        if printt:
            print('Axis Position {} [mm]'.format(answer))
        return answer

    def defineTimeZero(self, printt=True):
        self.sock.sendall((self.axis+'TP?\r').encode())
        answer = float(self.getReply().decode())
        if printt:
            print('Time Zero Position [mm] {}'.format(answer))
        self.timezeroPosition = answer


    def axisMoveAbsolute(self, target):
        self.sock.sendall((self.axis+'PA{}\r'.format(str(target))).encode())
        time.sleep(0.1)
        self.ismoving = True
        while self.ismoving:
            motionstatus = self.axisMotionStatus(printt=False)
            if motionstatus == 1:
                self.ismoving = False
            time.sleep(0.1)

        print('Finished moving')

    def axisMoveRelative(self, target):
        self.sock.sendall((self.axis + 'PR{}\r'.format(str(target))).encode())
        time.sleep(0.1)
        self.ismoving = True
        while self.ismoving:
            motionstatus = self.axisMotionStatus(printt=False)
            if motionstatus == 1:
                self.ismoving = False
            time.sleep(0.1)

        print('Finished moving')


"""
stage = newportESP301('192.168.140.200', 10001, 1)
stage.establishConnection()

stage.axisPosition()

try:
    if sys.argv[1] == 'ma':
        stage.axisMoveAbsolute(float(sys.argv[2]))
    elif sys.argv[1] == 'mr':
        stage.axisMoveRelative(float(sys.argv[2]))
    else:
        print("Type 'mr' for move relative and 'ma' for move absolute.\
                After this type the position in [mm].\n\
              'python newportesp301.py mr/ma distance/position' ")
    stage.axisPosition()
    stage.closeConnection()
        
except Exception as e:
    print(e)
    print("\nType 'mr' for move relative and 'ma' for move absolute.\n\
After this type the position in [mm].\n\
'python newportesp301.py mr/ma distance/position'\n")
    stage.closeConnection()
"""


