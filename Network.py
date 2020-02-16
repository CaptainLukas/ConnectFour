import socket

#https://wiki.python.org/moin/TcpCommunication

# vl nur einfach die ausgewählte Spalte schicken und jeder schaut sich selbst an wie der move wird
class EnhancedNetwork:
    __port=45688
    __buffersize=256
    __ip = ''

    def __init__(self,ip):
        self.__ip = ip
        return
    
    #def startNewConnection(ip,port,buffersize)
        #check ip is valid ip
        #check port is int
        #check buffersize is int
    #    return
    
    #def endConnection()
      #  self.__connection.close()
     #   return

    def sendMessage(self, message):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((self.__ip,self.__port))
        s.send(message.encode('utf-8'))
        s.close()
        return

    def receiveMessage(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind(('127.0.0.1',self.__port))
        s.listen(1)
        conn = s.accept()
        print('Connection')
        message = 'defaultMessage'
        while 1:
            message = conn.recv(self.__buffersize)
            if not message: break

        conn.close()
        s.close()
        return message
