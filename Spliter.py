def spliter(word):
    for i in word:
        print(i.upper(), end=".")

inp = input("Press Enter")

while inp != "exit":
    inp = input("\nSlplit text: ")
    spliter(inp)