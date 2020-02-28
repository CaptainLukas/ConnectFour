from Spielerfarbe import Spielerfarbe
class Spielfeld:

    # the matchfield
    # the matchfield is stored into a list of Spielerfarbe
    # the 6x7 field is stored in a straight list
    # each column is 6 fields long
    #
    # the matchfield as it is shown to the user
    #   1 2 3 4 5 6 7 columns
    #  5[][][][][][][]
    #  4[][][][][][][]
    #  3[][][][][][][]
    #  2[][][][][][][]
    #  1[][][][][][][]
    #  0[][][][][][][]
    # rows
    # the matchfield as it is stored in the list
    #    row: 0  1  2  3  4  5  0  1  2  3  4  5  0  1  2  3  4  5  0  1  2  3  4  5  0  1  2  3  4  5  0  1  2  3  4  5  0  1  2  3  4  5
    # column: 1  1  1  1  1  1  2  2  2  2  2  2  3  3  3  3  3  3  4  4  4  4  4  4  5  5  5  5  5  5  6  6  6  6  6  6  7  7  7  7  7  7
    #   list: [] [] [] [] [] []|[] [] [] [] [] []|[] [] [] [] [] []|[] [] [] [] [] []|[] [] [] [] [] []|[] [] [] [] [] []|[] [] [] [] [] []
    #  index: 0  1  2  3  4  5  6  7  8  9  10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41
    __field = list()

    # the players color
    farbe = Spielerfarbe

    # initialize a new instance of Spielfeld
    def __init__(self, farbe):
        self.__field= self.newField()
        self.farbe = farbe
        self.data=[]

    # sets a new matchfield
    # return:list returns an list with only Spielerfarbe.leer fields
    def newField(self):
        self.__field = list()
        i=0
        while (i < 42): # 41? bei 0 ist die erste Eintrag?- 42 stimmt schon, weil dann geht er wenn i 42 ist nicht mehr in die schleife, mit i 41 aber schon noch. mit i < 41 wird das letzte Listenelement ausgelassen. -Lukas
            self.__field.append(Spielerfarbe.leer)
            i += 1
        return self.__field

    # gets the matchfield if not None
    # return:list returns the matchfield
    def getField(self):
        if self.__field == None: # wie kann ein None entstehen?- in unserer anwendung theoretisch garnicht, hier geht es um allgemeine stabilität des Codes. Falls jemand fremder den code verwendet und von außen das __field auf None setzt, würde die Funktion sonst abstürzen.
            #Error werfen
            print('Error')

        return self.__field
    
    # gets the matchfield as two dimensional array of Spielerfarbe
    # return: the matchfield as two dimensional array
    def getFieldMatrix(self):
        matrixField = [][]
        return matrixField
    
    # gets the matchfield as string in printable order
    # return: the matchfield as string in printable order
    def getFieldString(self):
        stringField = ''
        return stringField
    
    # gets the sum of the markers in the matchfield
    # return: the sum of markers in the matchfield
    def getFieldSum(self):
        sum = 0
        return sum

    def getFieldTestMerge(self):
        return

    # this method adds a piece to the first free field in the selected column in the players color
    # column:int [1,7] the column selected to to add a piece
    # return:bool returns whether the move was valid
    def makeMove(self, column, color):
        if (column > 7 or column < 0):
            return False
        if (self.__field[column * 6 - 1] != Spielerfarbe.leer):
            return False
        else:
            i = (column - 1) * 6
            while i < 41:
                if (self.__field[i]==Spielerfarbe.leer):
                    check = self.__changeField(i,color)
                    if not check: return check
                    break
                i+=1
        return True

    # this method sets a field to the players color
    # index:int [0,41] the absolute index of the field to be set
    # return:bool returns whether the change was done
    def __changeField(self,index, color):
        if index > 41 or index < 0: # 42 ersetzt durch 41
            return False
        if self.__field[index] != Spielerfarbe.leer:
            return False
        self.__field[index] = color
        return True
