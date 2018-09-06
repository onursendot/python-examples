a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

list = set(a) & set(b)
print(list)

#-----------------------------------------------------------------
print("#-------------------------------------------------------")
import  random
randomList1 = random.sample(range(20), 10)
randomList2 = random.sample(range(20), 7)

list2 = set(randomList1) & set(randomList2)
print(list2)