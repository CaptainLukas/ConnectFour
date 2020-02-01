def PrintField(field):
    i = 5
    print('  1     2     3     4     5     6     7')
    while(i >=0):
        #print('['+str(i)+']' +'['+ str(i + 1 * 6)+']' + '['+str(i + 2 * 6)+ ']' + '[' + str(i + 3 * 6) + ']' + '[' + str(i + 4 * 6)+ ']' + '[' + str(i + 5 * 6) + ']' + '[' + str(i + 6 * 6) + ']')
        print('[' +field[i].name+ ']'+ '['+field[i+(1*6)].name+']' + '['+field[i+(2*6)].name+']'+ '['+field[i+(3*6)].name+']'+ '['+field[i+(4*6)].name+']'+ '['+field[i+(5*6)].name+']'+ '['+field[i+(6*6)].name+']')
        i-=1
    return

def PrintWin():
    return

def PrintLoss():
    return