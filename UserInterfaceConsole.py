from Spielerfarbe import Spielerfarbe
import os

def PrintField(field):
    os.system("cls")  # empty console
    i = 5
    print('  1     2     3     4     5     6     7')
    while(i >=0):
        #print('['+str(i)+']' +'['+ str(i + 1 * 6)+']' + '['+str(i + 2 * 6)+ ']' + '[' + str(i + 3 * 6) + ']' + '[' + str(i + 4 * 6)+ ']' + '[' + str(i + 5 * 6) + ']' + '[' + str(i + 6 * 6) + ']')
        print('[' +__printName(field[i])+ ']'+ '['+field[i+(1*6)].name+']' + '['+field[i+(2*6)].name+']'+ '['+field[i+(3*6)].name+']'+ '['+field[i+(4*6)].name+']'+ '['+field[i+(5*6)].name+']'+ '['+field[i+(6*6)].name+']')
        i-=1
    return

def __printName(farbe):
    if farbe == Spielerfarbe.leer:
        return ' '
    elif farbe == Spielerfarbe.gelb:
        return 'X'
    elif farbe == Spielerfarbe.rot:
        return 'O'
    else:
        return 'Fehler'

def PrintWin():
    os.system("cls")  # sollte Console leeren
    return

def PrintLoss():
    return

def PrintGetIPInfo():
    #empty console
    os.system("cls")
    print("Please enter IP to connect to:")
    return

def PrintGetPortInfo():
    print("Please enter port to connect to:")
    return

def Print(msg):
    print(msg)
    return

def PrintError(error):
    print('\033[93m' + error)