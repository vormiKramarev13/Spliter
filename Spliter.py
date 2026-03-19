import os
import time

def spliter(word):
    for i in word:
        print(i.upper(), end=".")

def clearConsole():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def main():

    inp = input(
        "\nWelcome to Spliter\n" 
        "This program split your entered text\n"
        "Press enter to start"
    )

    print(
        "-----------------------\n"
        "You can type 'exit' to quit program\n"
        "Type 'clear' to clean console"
        )   

    while True:

        inp = input("\nYour text: ")
    
        if inp == "clear":
            clearConsole()
        elif inp == "exit":
            print("\nGood Bye")
            time.sleep(1)
            break
        else:
            spliter(inp)

if __name__ == "__main__":
    main()