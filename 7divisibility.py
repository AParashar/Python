# Divisibility test by 7

def main():
    print("Function started!")
    inputData()
    result = processData(num)
    outputData(result)

def inputData():
    global num
    num = int(input("Input a number: "))

def processData(number):
    if(number % 7 == 0):
        return True
    else:
        return False

def outputData(result):
    if(result == True):
        print("This number is divisible by 7!")
    else:
        print("This number is not divisible by 7!")

main()