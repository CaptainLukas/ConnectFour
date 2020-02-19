import socket

#https://wiki.python.org/moin/TcpCommunication
#https://docs.python.org/3/howto/sockets.html

# vl nur einfach die ausgewählte Spalte schicken und jeder schaut sich selbst an wie der move wird
class EnhancedNetwork:
    __port=45688
    __buffersize=256
    __ip = ''
    __connection = socket
    __connectionStarted = False

    def __init__(self,ip):
        self.__ip = ip
        #AF_INET represents address and protocol family -> IPv4
        #SOCK_STREAM sets the socket type
        self.__connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        return

    def connectToOther(self):
        if self.__connectionStarted : return
        try:
            self.__connection.connect((self.__ip, self.__port))
            print('Connected')
            self.__connectionStarted = True
        except:
            print('Connection Failed')
        return

    def waitForConnection(self):
        if self.__connectionStarted: return
        try:
            self.__connection.bind(('127.0.0.1', self.__port))
            self.__connection.listen(1)
            self.__connection, addr = self.__connection.accept()
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
            message = 'CON4'+ message.encode('utf-8').len + 'E'+ message
            self.__connection.send(message.encode('utf-8'))
        except:
            print('Sending message failed.')
        return

    def receiveMessage(self):
        chunks = []
        bytes_recd = 0
        messagelen = 0
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
        while(chunk != bytes('E','utf-8')):
            chunk = self.__connection.recv(1)
            if chunk == bytes('E','utf-8'):
                break
            bytenumbers = bytenumbers+ chunk

        number = bytenumbers.decode('utf-8')

        while bytes_recd < number:
            chunk = self.__connection.recv(min(number-bytes_recd, 2048))
            print(chunk)
            if chunk == b'':
                raise RuntimeError("socket connection broken")
            chunks.append(chunk)
            bytes_recd = bytes_recd + len(chunk)
        return b''.join(chunks)
