import msvcrt
# to get this working in PyCharm you need to change the Run Config as following:
#'Run' -> 'Edit Configurations' -> check 'Emulate terminal in output console'

# Gets the next pressed key of the user and returns it as a string
def GetUserinput():
    while True:
        try:
            key = msvcrt.getch()
            key = key.decode("utf-8")
        except UnicodeDecodeError:
            print('please try another key')
            #read one key that is in queue due to the error and is not an input from the user
            msvcrt.getch()
            continue
        print(key)
    return key