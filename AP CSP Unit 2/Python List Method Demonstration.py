import random as r
#1: Summing ALL List Items
nums = []
while True:
    usernum = int(input("Enter a number (type 0 to stop): "))
    if usernum == 0:
        break
    nums.append(usernum)
total = sum(nums)
print("The total is:", total)

#2: Multiplication of ALL List Items
nums = []
while True:
    usermult = int(input("Enter a number (type 0 to stop): "))
    if usermult == 0:
        break
    result = 1
    nums.append(usermult)
for num in nums:
    result *= num
print("Total multiplied: ", result)

#3: Highest Number Function
li1 = []
for x in range(15):
    li.append(r.randint(15))
high = li[0]
for y in range(len(li)):
    if li [y] > high:
        high = li[y]
print(high)

#4: Minimum Number Function
li = []
for x in range(15):
    li.append(r.randint(15))
low = li[0]
for y in range(len(li)):
    if li [y] < low:
        low = li[y]
print(low)

#5: Duplicate Checker
newlist = []
for x in range(15):
    li.append(r.randint(15))
for x in range(len(newlist)):
    if li [x] not in newlist:
        newlist.append(li[x])
print(newlist)

#6: Empty or Not? List Checker
li.clear()
if len(li) == 0:
    print(True)
else:
    print(False)

#7: Clone & Duplicate A List
newlist2 = []
for x in range(15):
    newlist2.append(r.randint(15))
newlist3 = newlist2.copy()
print(newlist2)
print(newlist3)

#8: Given List of Words - Determining Length
wordlist = ['possible', 'distortion', 'pollution', 'impact', 'inject', 'motivation', 'bubble']
n = 6
longWords = [word for word in words if len(word) > n]
print(longWords)

#9: Checking If There's A Common Member of Lists
compare1 = []
compare2 = []
for x in range(8):
    compare1.apppend(r.randint(8))
for y in range(8):
    compare2.append(r.randint(8))
for a in compare1:
    for b in compare2:
        if a == b:
            result == True
        else:
            result == False
print(result)

#10: Removing Specific Indices of Items
colors = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
=colors = [x for i, x in enumerate(colors) if i not in (0, 4, 5)]
print(colors)

#11: List Reversal
aList = [100, 200, 300, 400, 500]
aList.reverse()
print.aList()

#12: Squaring All List Items
aList=[1,2,3,4,5,6,7]
squared = [x ** 2 for x in aList]
print(squared)

#13: Remove and Replace with 200
List1 = [5, 10, 15, 20, 25, 50, 20]
index = List1.index(20)
List1[index] = 200
print(List1)

#14: Remove 20
List1 = [5, 10, 15, 20, 25, 50, 20]
newList = [x for x in List1 if x != 20]
print(newList)
