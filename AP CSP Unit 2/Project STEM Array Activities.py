# Activity 1: Temperature List
temperatures = []
for x in range(5):
    temp = input("Enter a temperature: ")
    temperatures.append(temp)
print(temperatures)

# Activity 2: "Nums" List
nums = [56, 25, -28, 11, -6]
print(nums[0])
print(nums[len(nums)-1])

# Activity 3: Word List
w = ["Algorithm", "Logic", "Filter", "Software", "Network", "Parameters", "Analyze", "Algorithm", "Functionality", "Viruses"]
for x in range(len(w)):
    print(str(x), ": ",  w[x], ", ", str(len(w[x])))

# Activity 4: Lowercase Computing List
w = ["Algorithm", "Logic", "Filter", "Software", "Network", "Parameters", "Analyze", "Algorithm", "Functionality", "Viruses"]
new_w = [item.lower() for item in w]
print(new_w)

# Activity 5: F and L Lists
w = ["Algorithm", "Logic", "Filter", "Software", "Network", "Parameters", "Analyze", "Algorithm", "Functionality", "Viruses"]
letter = "F", "L"
for x in w:
    if x.startswith(letter):
        print(x)

# Activity #6: Random List
import random
numbers = []
numberValues = int(input("How many values to add to the list: "))
for x in range(numberValues):
    numbers.append(random.randint(99,199))
    numbers.sort()
print(numbers)

# Activity 7: Revised with Negatives
import random
numbers = []
numberValues = int(input("How many values to add to the list: "))
for x in range(numberValues):
    numbers.append(random.randint(99,199))
    numbers.sort()
negativeList = [x * -1 for x in numbers]
print(negativeList)
print("Total: ", sum(negativeList))