import Spielerfarbe
class Spielfeld:
    __field = list()
    def __init__(self):
        _field= self.newField()
        self.data=[]
    def newField(self):
        #_field = list()
        i=0
        while (i < 42):
            self.append(Spielerfarbe.leer)
            i += 1
        return self._field