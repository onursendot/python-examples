rock = 0
paper = 1
scissors = 2

while True:
    import random
    rand = random.sample(range(3), 1)
    userInput = int(input("Type your move\n0-Rock\n1-Paper\n2-Scissors\n:"))

    if userInput ==0:
        if rand[0] ==0:
            print("Draft")
        elif rand[0] ==1:
            print("You lost")
        elif rand[0]==2:
            print("You won")
    elif userInput ==1:
        if rand[0] ==0:
            print("You won")
        elif rand[0] ==1:
            print("Draft")
        elif rand[0]==2:
            print("You lost")
    elif userInput ==2:
        if rand[0] ==0:
            print("You lost")
        elif rand[0] ==1:
            print("You won")
        elif rand[0]==2:
            print("Draft")
    else:
        print("Invalid input, try again.")

    if input("Do you want to start a new game? (y/n): ") == "n":
        break
