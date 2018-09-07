word = input("Enter a text:")
wordList = []

for x in word:
    wordList.append(x)

reversedList = wordList[::-1]

if wordList == reversedList:
    print("palindrome")
else:
    print("not palindrome")