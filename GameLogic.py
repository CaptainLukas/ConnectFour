from Spielfeld import Spielfeld
from Spielerfarbe import Spielerfarbe as sf
import UserInterfaceConsole as ui
import ControlsConsole
from Network import EnhancedNetwork
import ControlsConsole as cc
from Network import EnhancedNetwork

class GameLogic:

    __matchfield = Spielfeld
    __connection = EnhancedNetwork

    def __init__(self):
        self.__matchfield = Spielfeld(sf.gelb)
        self.__connection = EnhancedNetwork('192.168.1.86')
        self.data=[]

    def startGame(self):
        #self.__matchfield = Spielfeld(sf.gelb)
        self.__matchfield.newField()

        self.testgame()
        #you want to connect or be connected?
        #start connection as client or server
        self.startConnection()
        #start game
        return

    def testgame(self):
        ui.PrintField(self.__matchfield.getField())
        self.__matchfield.makeMove(3, sf.gelb)
        self.__matchfield.makeMove(4,sf.rot)
        self.__matchfield.makeMove(4, sf.gelb)
        self.__matchfield.makeMove(3, sf.rot)
        ui.PrintField(self.__matchfield.getField())
        return
    
    def startConnection(self):
        ui.PrintGetIPInfo()
        ip = cc.GetUserInputString()
        #ui.PrintGetPortInfo()
        #port = cc.GetUserInputString()
        network = EnhancedNetwork(ip)
        network.connectToOther()
        #network.waitForConnection()
        #network.sendMessage("Hello World")
        print(network.receiveMessage())
        network.endConnection()
        
