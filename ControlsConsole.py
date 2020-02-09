import msvcrt

#Funktioniert nicht in PyCharm nur in der Konsole
def GetUserinput():
    while True:
        c = msvcrt.getch()
        c = c.decode("utf-8")
        print(c + ' was pressed')
        if c=='q':
            break
    return c