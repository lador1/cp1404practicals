
numbers = []
for i in range(5):
    numbers_chosen = int(input("Number: "))
    numbers.append(numbers_chosen)

print('The first number entered is', numbers[0])
print('The last number entered is', numbers[-1])
print('The smallest number is', min(numbers))
print('The smallest number is', max(numbers))
print('The average of the numbers is', sum(numbers) / len(numbers))



usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn',
             'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']

username = input("What is your username?: ")
if username in usernames:
    print("Access granted!")
else:
    print("Access denied!")

