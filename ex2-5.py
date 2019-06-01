#
valid_status = True

while valid_status:
    try:
        money_amount = int(input("Please enter Dollar amount: "))
        valid_status = False
    except:
        print("Invalid Entry. Try again!")
        valid_status = True

print("You're carrying Rupees: ", money_amount*72)