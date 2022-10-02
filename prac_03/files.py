#1
users_name = input('What is your name?: ')
out_file = open("name.txt", 'w')
print(users_name, file=out_file)
# out_file.close

#2
in_file = open('name.txt', 'r')
name = in_file.read().strip()
in_file.close()
print("Your name is", name)

#3
in_file = open('numbers.txt', 'r')
number1 = int(in_file.readline())
number2 = int(in_file.readline())
number3 = number1 + number2
print(number3)
in_file.close()

4
in_file = open('numbers.txt', 'r')
lines = in_file.readlines()
print(lines)
in_file.close()