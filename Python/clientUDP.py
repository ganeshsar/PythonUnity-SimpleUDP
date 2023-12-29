import socket
import time

class ClientUDP:
    def __init__(self,ip,port, autoReconnect = True) -> None:
        self.ip = ip
        self.port = port
        self.autoReconnect = autoReconnect
        self.connected = False
        pass

    def sendMessage(self,message):
        try:
            message = str('%s<EOM>'%message).encode('utf-8')
            self.socket.send(message)
        except ConnectionRefusedError as ex:
            print("Connection refused. Is server running?")
            self.disconnect()
        except ConnectionResetError as ex:
            print("Server was disconnected...")
            self.disconnect()

    def disconnect(self):
        self.connected = False
        self.socket.close()
        if(self.autoReconnect):
            time.sleep(1)
            self.connect()

    def connect(self):
        try:
            self.socket = socket.socket(socket.AF_INET, 
                                        socket.SOCK_DGRAM)     
            print("Attempting Connection...")
            self.socket.connect((self.ip, self.port))
            print("Will send messages to "+str(self.socket.getpeername()))
            self.connected = True
        except ConnectionRefusedError as ex:
            print("Connection refused. Is server running?")
            self.disconnect()
        except ConnectionResetError as ex:
            print("Server was disconnected...")
            self.disconnect()
        