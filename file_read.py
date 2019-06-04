# Read content from the file

# Method 1 : Needs no closing 
with open("read-write.txt", mode="r") as my_file:
    for line in my_file:
        print(line)

# Method 2
the_file = open("read-write.txt", mode="r")
print("File name is: ",the_file.name)
file_lines = the_file.readlines()                # Returns an array of all the lines + new line character included
print(file_lines)
the_file.close()