import Spielerfarbe
class Spielfeld:
    __field = list()
    farbe = Spielerfarbe
    def __init__(self):
        self._field= self.newField()
        self.data=[]
    def newField(self):
        self.__field = list()
        i=0
        while (i < 42):
            self.__field.append(Spielerfarbe.leer)
            i += 1
        return self.__field

    def getField(self):
        if self.__field == None:
            #Error werfen
            pass

        return self.__field

    def makeMove(self, row):
        if (row > 7):
            return False
        if (self.__field[row*6-1] != Spielerfarbe.leer):
            return False
        else:
            i = (row -1) * 6
            while i < 42:
                if (self.__field[i]==Spielerfarbe.leer):
                    check = self.__changeField(i)
                    if not check: return check
                i+=1
        return True

    def __changeField(self,index):
        if index > 41: return False
        if self.__field[index] != Spielerfarbe.leer: return False
        self.__field[index] = self.farbe
        return True