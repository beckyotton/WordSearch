# Create a function that takes 2 numbers and returns True if their product is greater than 25.
number = 0


def add(number1, number2):
    number = int(number1) + int(number2)
    if number > 25:
        return True
    else:
        return False


number1 = input("number 1")
number2 = input("number 2")
print(add(number1, number2))

# Create a file using open() and then write every odd number between 1-10 on seperate lines in the file.

f = open("uneven.txt", "a")
for i in range(1, 10):
    if i % 2 != 0:
        f.write(str(i)+"\n")
f.close()

# Create a function that reads the file in 2. and returns the sum of all the numbers.


f = open("uneven.txt", "r")
value = f.readlines()
sum = 0
for i in range(0, 5):
    sum += int(value[i])

print(sum)


# Create a function that writes a random number to a file, asks the user to guess a number, and then checks
# if the user guessed the correct number by reading the file.

from random import *




