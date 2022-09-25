# FOR ODD NUMBERS BETWEEN 1-20
for i in range(1, 21, 2):
    print(i, end=' ' )
print()

# A
for i in range(0, 101, 10):
    print(i, end=' ')
print()

# B
for i in range(20, 0, -1):
    print(i, end=' ')
print()

# C
number_of_stars = int(input("Enter a number:"))
print(f"Number of stars: {number_of_stars}")
for i in range(number_of_stars):
    print('*', end=' ')

# D
number_of_stars = int(input("Enter a number:"))
print(f"Number of stars: {number_of_stars}")
for i in range(1, number_of_stars + 1, +1):
    print('*' * i)