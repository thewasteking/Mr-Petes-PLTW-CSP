# 1: Grandma Ester's Cookies
# Gather input of how old the user is
age = int(input("How old are you turning? "))
# initialize the count variable
x = 0
# repeat # of times in age
while x < age:
    print("(::)")
    x += 1
# confirm and celebrate age
print("Grandma Ester baked you ", age , " cookies. Bon appetit!")

# 2: While Loop for values 4-24
x = 4
while x <= 24:
    print(x)
    x += 4

# 3: Word Game
x = 0
while x >= 0:
    x += 1
    word = input("Please enter a word: ")
    print("You entered the word: ", word)
    if word == "DONE":
        print("A total of ", x, "words were entered.")
        break

#4: Numbers 35-45
for x in range(35,46):
    print(x, end=" ")

#5: Numbers 26-41:
print()
for x in range(26,41):
    print(x, end=" ")

#6: Counting By 7
print()
for x in range (0, 84, 7):
    print(x, end=" ")

#7: Counting Backwards By 6:
print()
for x in range(76, 28, -6):
    print(x, end=" ")

#8: Summing Adding By 7s
print()
total = 0
for x in range(7, 71, 7):
    total += x
print(total)

#9: Summing Adding Steps Of 5 
total = 0
for x in range(15, 51, 5):
    total += x
    print("Added: ", x)
    print("Total: ", total)

#10: Summing Adding Steps of 1
total = 0
for x in range(105, 0, -1):
    total += x
    print("Added: ", x)
    print("Total: ", total)

#11: Adding 7 Ages
total = 0
for x in range(7):
    age = int(input("Enter an age: "))
    total += age
    print("The sum of all ages is: ", total)