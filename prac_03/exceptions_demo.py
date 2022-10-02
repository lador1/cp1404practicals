"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
2. When will a ZeroDivisionError occur?
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")

#1 When the numerator or denominator and not integers or valid numbers, such as a decimal (50.2) or text and symbols

#2 When the demoninator entered is zero, this is because a number devided by zero is zero

#3 Was unable too, Im starting to think its not possible without breaking DRY. I tried a while loop but it infinitely printed the values and I couldt get it to stop.