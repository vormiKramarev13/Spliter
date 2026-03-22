import os
import time

def spliter(word="_",dot="."):
    lastprintword = ""
    for i in word:
        printword = i.upper() + dot
        print(printword, end="")
        lastprintword = lastprintword + printword
    return lastprintword

    

def clearConsole():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def exitProgram():
    print("\nGood Bye")
    time.sleep(1)

def selectSpace():
    selectedspace = input("Type space: ")
    return selectedspace

def printCmdList():
    print("""
/select.space - Selecting space for splited words
/exit - Exit program
/clear - Clean your console
/history - Check your history
""")

def displayHistory(listik):
    print()
    for i in listik:
        print(i)

def main():

    selectdot = "."

    inp = input(
        "\nWelcome to Spliter\n" 
        "This program split your entered word\n"
        "Press enter to start"
    )

    print("""
-----------------------
Type '/help' to get command list
""")   

    history = []

    while True:

        inp = input("\nYour word: ")
    
        if inp == "/clear":
            clearConsole()
        elif inp == "/exit":
            exitProgram()
            break
        elif inp == "/select.space":
            selectdot = selectSpace()
        elif inp == "/help":
            printCmdList()
        elif inp == "/history":
            displayHistory(history)
        elif " " in inp:
            print("Words, no sentence and texts")
        else:
            lastprint = spliter(inp,dot=selectdot)
            history.append(lastprint)

if __name__ == "__main__":
    main()