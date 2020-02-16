from Spielfeld import Spielfeld
from Spielerfarbe import Spielerfarbe as sf
import UserInterfaceConsole as ui
import ControlsConsole
from Network import EnhancedNetwork

class GameLogic:

    __matchfield = Spielfeld

    #def __init__(self):
    #    self.data=[]

    def startGame(self):
        self.__matchfield = Spielfeld(sf.gelb)
        self.__matchfield.newField()

        self.testgame()
        ControlsConsole.GetUserinput()
        network = EnhancedNetwork('192.168.1.86')
        for i in range(1,10):
            network.sendMessage("Hello World")
            print(network.receiveMessage())
        return

    def testgame(self):
        ui.PrintField(self.__matchfield.getField())
        self.__matchfield.makeMove(3, sf.gelb)
        ui.PrintField(self.__matchfield.getField())
        self.__matchfield.makeMove(4,sf.rot)
        ui.PrintField(self.__matchfield.getField())
        self.__matchfield.makeMove(4, sf.gelb)
        self.__matchfield.makeMove(3, sf.rot)
        self.__matchfield.makeMove(3, sf.gelb)
        self.__matchfield.makeMove(4, sf.rot)
        self.__matchfield.makeMove(5, sf.gelb)
        ui.PrintField(self.__matchfield.getField())
        self.__matchfield.makeMove(2, sf.rot)
        ui.PrintField(self.__matchfield.getField())
        return
