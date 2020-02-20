import socket

#https://wiki.python.org/moin/TcpCommunication
#https://docs.python.org/3/howto/sockets.html

# NETWORK PROTOCOL
# Header(CON4)|Payloadlength|E|Payload
#ExampleMessage:
# CON45EHello
class EnhancedNetwork:
    __port=45688
    __ip = '192.168.1.86'
    __connection = socket
    __connectionStarted = False

    def __init__(self):
        #AF_INET represents address and protocol family -> IPv4
        #SOCK_STREAM sets the socket type
        self.__connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        return

    #connects to the other player
    def connectToOther(self, ip):
        self.__ip = ip
        if self.__connectionStarted : return
        try:
            self.__connection.connect((self.__ip, self.__port))
            print('Connected')
            self.__connectionStarted = True
        except:
            print('Connection Failed')
        return

    #waits for other player to connect
    def waitForConnection(self):
        if self.__connectionStarted: return
        try:
            #bind socket to ipv4 address of pc
            self.__connection.bind((socket.gethostname(), self.__port))
            #wait for one client to connect
            self.__connection.listen(1)
            (self.__connection, addr) = self.__connection.accept()
            print('Connected')
            self.__connectionStarted = True
        except:
            print('Connection Failed')
        return

    #closes connection
    def endConnection(self):
        if not self.__connectionStarted: return
        self.__connection.close()
        print('Connection closed')
        return

    #sends message to connection
    def sendMessage(self, message):
        if not self.__connectionStarted: return
        try:
            #add header and length info
            message = 'CON4'+ str(len(message.encode('utf-8'))) + 'E'+ message
            #send complete message
            self.__connection.send(message.encode('utf-8'))
        except:
            print('Sending message failed.')
        return

    def receiveMessage(self):
        chunks = []
        bytes_recd = 0
        messagelen = 0

        #this loop checks for the header at the beginning of the message
        while(True):
            chunk = self.__connection.recv(1)
            if chunk != bytes('C','utf-8'):
                continue
            chunk = self.__connection.recv(1)
            if chunk != bytes('O','utf-8'):
                continue
            chunk = self.__connection.recv(1)
            if chunk != bytes('N','utf-8'):
                continue
            chunk = self.__connection.recv(1)
            if chunk != bytes('4','utf-8'):
                continue
            break

        bytenumbers=b''
        #reads the length of the payload
        while(chunk != bytes('E','utf-8')):
            chunk = self.__connection.recv(1)
            if chunk == bytes('E','utf-8'):
                break
            bytenumbers = bytenumbers+ chunk

        number = int(bytenumbers.decode('utf-8'))
        #read payload
        chunk = self.__connection.recv(number)
        return chunk.decode('utf-8')
