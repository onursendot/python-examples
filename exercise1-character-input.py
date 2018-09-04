name = input("Enter your name:")
age = int(input("Enter your age:"))

import datetime
year = datetime.datetime.now().year
howManyYearsAfter = (100-age)

text = "Dear %s, in %d you will be 100 years old." % (name,(year+howManyYearsAfter))
print(text)

# Extras 1 and 2
copyNumber = int(input("Enter the number of copies:"))
print(copyNumber * (text+"\n"))