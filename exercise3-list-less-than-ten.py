a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

userNumber = int(input("Choose a number:"))

newList = []
i = 0
while i<len(a):
    if(a[i]<userNumber):
        newList.append(a[i])
    i+=1

print(newList)
