from Spielfeld import Spielfeld
from Spielerfarbe import Spielerfarbe as sf
import UserInterfaceConsole as ui
<<<<<<< HEAD
import ControlsConsole
from Network import EnhancedNetwork
=======
import ControlsConsole as cc
From Network import EnhancedNetwork
>>>>>>> 7e82657fc57c353e093e8a9789f9bab02826d589

class GameLogic:

    __matchfield = Spielfeld
    __connection = EnhancedNetwork

    def __init__(self):
        self.__matchfield = Spielfeld()
        self.__connection = EnhancedNetwork()
        self.data=[]

    def startGame(self):
        #self.__matchfield = Spielfeld(sf.gelb)
        self.__matchfield.newField()

        self.testgame()
<<<<<<< HEAD
        ControlsConsole.GetUserinput()
        network = EnhancedNetwork('192.168.1.86')
        for i in range(1,10):
            network.sendMessage("Hello World")
            print(network.receiveMessage())
=======
        self.startConncetion()
        
>>>>>>> 7e82657fc57c353e093e8a9789f9bab02826d589
        return

    def testgame(self):
        ui.PrintField(self.__matchfield.getField())
        self.__matchfield.makeMove(3, sf.gelb)
        self.__matchfield.makeMove(4,sf.rot)
        self.__matchfield.makeMove(4, sf.gelb)
        self.__matchfield.makeMove(3, sf.rot)
        ui.PrintField(self.__matchfield.getField())
        return
    
    def startConnection():
        ui.PrintGetIPInfo()
        ip = cc.GetUserInputString()
        ui.PrintGetPortInfo()
        port = cc.GetUserInputString()
        self.__conncetion.startNewConnection(ip,port,30)#30?
        self.__connection.sendMessage('startGame')
        
