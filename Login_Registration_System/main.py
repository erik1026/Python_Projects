from os import getcwd
import glob
import sys

def get_platform():
    platforms = {
        'linux1' : 'Linux',
        'linux2' : 'Linux',
        'darwin' : 'OS X',
        'win32' : 'Windows'
    }

    if sys.platform not in platforms:
        return sys.platform
    
    return platforms[sys.platform]

def userPrompt():
    print(f'Please select from one of the following options.')
    print(f'1. Login\n2. Register\n3. Reset Password\n4. Exit program')

def doesUserExist(splitUserName):

    sysPlatform = get_platform()
    if sysPlatform == 'Windows':
        slash = "\\"
    else:
        slash = "/"

    userName = splitUserName[0] + splitUserName[1] + ".txt"

    currentDir = getcwd() + slash
    filesInCurrentDir = glob.glob(currentDir + "*.txt")
    if filesInCurrentDir:
        for file in filesInCurrentDir:
            splitFilePath = file.split(slash)
            lengthOfPath = len(splitFilePath)
            if(splitFilePath[lengthOfPath - 1] == userName):
                return True
        
    return False

def login():
    pass
 
def registerUser():

    userName = input("Enter your first and last name: ")
    splitUserName = userName.split(sep=" ")
    userExist = doesUserExist(splitUserName)
    
    if(userExist):
        print(f'User already exists. Please select another option...')
    else:
        fileName = splitUserName[0] + splitUserName[1] + '.txt'
        password = input("Enter the password you would like to use: ")
        with open(fileName, 'w') as file:
            file.write(userName+'\n')
            file.write(password)
            file.close()


def main():

    userInput = "0"
    while(userInput != "4"):
        userPrompt()
        userInput = input("Option: ")

        if (userInput == "1"):
            pass
        elif (userInput == "2"):
            print(f'Registering...')
            registerUser()
            
        elif (userInput == "3"):
            pass
        elif (userInput == "4"):
            pass
        else:
            print(f'Please re-enter a valid option...')

    print(f'Exiting program...\nGoodbye!')
    

if __name__ == "__main__":
    main()