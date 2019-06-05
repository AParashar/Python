input_status = True
item_list = []

while input_status:
    try:
        item = input("Enter item: ")
        if(item != ''):
            input_status = True
            item_list.append(item)
        else:
            break
    except:
        print("Enter a valid item name!")
        input_status = True

print(item_list)

# Bubble Sort Algorithm
n = len(item_list)
for i in range(n):
    swapped = False
    for j in range(0, n-i-1):
        if item_list[j] > item_list[j+1] : 
            item_list[j], item_list[j+1] = item_list[j+1], item_list[j] 
            swapped = True
    if swapped == False: 
        break
print(item_list)