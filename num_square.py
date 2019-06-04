nmuber = int(input("Enter a number: "))

for num in range(1, nmuber+1):
    print("{0} squared is {1:>3}".format(num, num**num))