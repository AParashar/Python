def input_vakya():
    global vakya, shabd
    vakya = input("Input a senetence: ")
    shabd = input("Enter a letter to find: ")

def search(vakya):
    # for letter in vakya:
    #     print(letter)
    #     if(letter == shabd):
    #         return True
    found = False
    for index in range(len(vakya)):
        if(shabd == vakya[index]):
            found = True
            return found


def main():
    input_vakya()
    found = search(vakya)
    print(found)

main()