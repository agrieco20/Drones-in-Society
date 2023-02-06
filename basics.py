# Author: Anthony Grieco
# Date: 2/6/2023
#
# Description: This brief program offers a foundation for the basics of Python, which will later be necessary in order to fly drones

# Basic Math and Console Output Examples
a = 5+5
print(a)
print(12)
print("Hello World!")

# Basic Input and String Conversion Examples
name = input("What is your name? ")
age = int(input("What is your age? "))
print("Hello, " + name + "!")
print("You are " + str(age) + " years old.")
agePlus5 = age + 5
print("You will be " + str(agePlus5) + " years old in 5 years.")

# Conditional Statement Examples
if age > 23:
    print("You're REALLY old!")

elif age < 23:
    print("You're REALLY young!")

else:
    print("Okay.")

# Repetition Examples

# For Loop
for i in range(10):
    print(i + 1)

print("Done!")