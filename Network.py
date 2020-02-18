import socket

#https://wiki.python.org/moin/TcpCommunication

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
            self.__connection = self.__connection.accept()
            print('Connected')
            self.__connectionStarted = True
        except:
            print('Connection Failed')
        return

    #closes connection
    def endConnection(self):
        if not self.__connectionStarted: return
        self.__connection.close()
        return

    #sends message to connection
    def sendMessage(self, message):
        if not self.__connectionStarted: return
        try:
            self.__connection.send(message.encode('utf-8'))
        except:
            print('Sending message failed.')
        return

    #receives message from connection
    def receiveMessage(self):
        if not self.__connectionStarted: return
        try:
            print('Connection')
            message = 'defaultMessage'
            while 1:
                message = self.__connection.recv(self.__buffersize)
                if not message: break
        except:
            print('Receiving message failed.')
        return message
