import Spielfeld
import UserInterfaceConsole as ui

class GameLogic:
    
    __matchfield = Spielfeld

    #def __init__(self):
    #    self.data=[]

    def startGame(self):
        __matchfield = Spielfeld()
        __matchfield.newField()
        self.game()
        return

    def game(self):
        ui.PrintField(self.__matchfield.getField())
        return
