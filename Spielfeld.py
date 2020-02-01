import Spielerfarbe
class Spielfeld:

    # the matchfield
    __field = list()

    # the players color
    farbe = Spielerfarbe

    # initialize a new instance of Spielfeld
    def __init__(self, farbe):
        self._field= self.newField()
        self.fatbe = farbe
        self.data=[]

    # sets a new matchfield
    # return:list returns an list with only Spielerfarbe.leer fields
    def newField(self):
        self.__field = list()
        i=0
        while (i < 42):
            self.__field.append(Spielerfarbe.leer)
            i += 1
        return self.__field

    # gets the matchfield if not None
    # return:list returns the matchfield
    def getField(self):
        if self.__field == None:
            #Error werfen
            pass

        return self.__field

    # this method adds a piece to the first free field in the selected column in the players color
    # column:int [1,7] the column selected to to add a piece
    # return:bool returns whether the move was valid
    def makeMove(self, column):
        if (column > 7 or column < 0):
            return False
        if (self.__field[column * 6 - 1] != Spielerfarbe.leer):
            return False
        else:
            i = (column - 1) * 6
            while i < 42:
                if (self.__field[i]==Spielerfarbe.leer):
                    check = self.__changeField(i)
                    if not check: return check
                i+=1
        return True

    # this method sets a field to the players color
    # index:int [0,41] the absolute index of the field to be set
    # return:bool returns whether the change was done
    def __changeField(self,index):
        if index > 41 or index < 0: return False
        if self.__field[index] != Spielerfarbe.leer: return False
        self.__field[index] = self.farbe
        return True