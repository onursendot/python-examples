number = int(input("Enter a number:"))

if number%2==0:
    if number%4==0:
        print("Your number is even and multiple of 4")
    else:
        print("Even")
else:
    print("Odd")

num = int(input("Which number do you want to check:"))
check = int(input("Type a number to divide:"))

if num%check == 0:
    print("The number %d divides evenly with %d" % (num, check))
else:
    print("The number %d doesn't divide evenly with %d" % (num, check))