a = int(input("Enter a number:"))

divisors = []
rand = range(1,(a+1))
for i in rand:
    if a%i == 0:
        divisors.append(i)

print(divisors)

