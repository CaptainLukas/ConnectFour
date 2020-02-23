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
        self.__connection = EnhancedNetwork()
        self.data=[]

    def startGame(self):
        #self.__matchfield = Spielfeld(sf.gelb)
        self.__matchfield.newField()

        #self.testgame()
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

        #if not self.__connection.connectToOther(ip): return
        #self.__connection.waitForConnection()
        #self.__connection.sendMessage("Hello World")
        while(True):
            inp = cc.GetUserInputChar()
            if inp == 'c':
                ui.PrintGetIPInfo()
                ip = cc.GetUserInputString()
                if not self.__connection.connectToOther(ip):
                    ui.PrintError('connection error')

            if inp == 'g':
                if not self.__connection.waitForConnection():
                    ui.PrintError('connection error')

            if inp == 's':
                ui.Print('input message:')
                message = cc.GetUserInputString()
                self.__connection.sendMessage(message)

            if inp == 'r':
                print(self.__connection.receiveMessage())
            if inp == 'e':
                self.__connection.endConnection()
                break
        
