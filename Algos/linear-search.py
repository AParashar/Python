# Linear search Algorithm

sample_list = ['one', 2, "Three", "$", "%", 6]

search_key = input("Enter any Word / Letter to search:  ")
# Python takes input only in string format

position = 0
found = False

while(position < len(sample_list) and not found):
    # print("Loop: ", position)
    if(sample_list[position] == search_key):
        print("The entered search word Exists at index {0} in the list!".format(position))
        found = True
    position = position + 1

if(not found):
    print("No such item exist in the list!")

    # If no item found then add item to the list
    sample_list.extend([search_key])
    # print(sample_list)