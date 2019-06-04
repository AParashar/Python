def prompt_user():
    user_name = input("Enter user name to check: ")
    password = input("Enter password: ")
    return user_name, password

def check_user(lists, user, password):
    for index, element in enumerate(lists):
        if(element.split()[0] == user and element.split()[1] == password):
            return "Your login is successful"

        elif(element.split()[0] == user and element.split()[1] != password):
            return "Incorrect password"
            
        elif(element.split()[0] != user):
            if(index < len(lists) - 1):
                pass
            else:
                return "This username does not exist"


def main():
    user_name, password = prompt_user()

    with open("user-pass.txt", mode="r") as my_file:
        line = my_file.read().splitlines()
    
    text = check_user(line, user_name, password)
    print(text)



main()