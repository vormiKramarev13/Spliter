def spliter(word):
    for i in word:
        print(i.upper(), end=".")

inp = input("Press Enter to continue")

while inp != "exit":
    inp = input("\nSplit text: ")
    spliter(inp)