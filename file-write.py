# Write the contents to a file

animals = ['Jaguar', 'Python', 'Jackal']
# with open("read-write.txt", mode="a") as my_file:    # Appends data to an already existing content of the file
# # with open("read-write.txt", mode="w") as my_file:
#     for animal in animals:
#         my_file.write('\n' + animal)
#         # my_file.append(animal + '\n')

animals = []

# Read content from an already existing file
with open("read-write.txt", mode = "r") as animal_list:
    for animal in animal_list:
        animals.append(animal.rstrip())


# Sort the contents alphabatically
n = len(animals)
for i in range(n):
    swapped = False
    for j in range(n-i-1):
        if animals[j].lower() > animals[j+1].lower(): 
            animals[j], animals[j+1] = animals[j+1], animals[j] 
            swapped = True
    if swapped == False: 
        break
    
# Write sorted content to the file
print(animals)
with open("read-write.txt", mode = "w") as my_file:
    for animal in animals:
        my_file.write(animal + "\n")

