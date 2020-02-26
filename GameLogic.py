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

    def game(self):
    {
        self.ui.PrintConnectionInfo()#noch zu implementieren
        connInfo = cc.GetConnectionInfo()#noch zu implementieren
        self.__startConnection(connInfo)
        #übergeben ob erster oder zweiter
        self.__startGame()#connInfo gleich als indikator für ersten und zweiten?
        
    }
    
    def __startGame(self, first):
        over = False
        self.__matchfield.newField()
        if (first):
            #startfirst()
        else:
            #startseconde()
        while(not over)
        {
            #Spielablauf
        }
        return
    
    def __startConnection(self, asServer):

        #wenn asServer true, dann 
        #waitfor connection
        #if not self.__connection.waitForConnection():
            #ui.PrintError('connection error')
        #else
        #connect to
        #ui.PrintGetIPInfo()
        #ip = cc.GetUserInputString()
        #if not self.__connection.connectToOther(ip):
            #ui.PrintError('connection error')
        
        #verbunden, jetzt Spiel starten
        #herausfinden wer beginnt
        #startgame
        
        
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
