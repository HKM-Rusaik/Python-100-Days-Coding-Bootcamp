# student_heights = input().split()
# for n in range(0, len(student_heights)):
#     student_heights[n] = int(student_heights[n])

# total_height = 0
# for height in student_heights:
#     total_height += height

# print(f"total height = {total_height}")

# number_of_students = 0
# for student in student_heights:
#     number_of_students += 1

# print(f"number of students = {number_of_students}")

# average_height = (total_height/number_of_students)
# print(f"average height {average_height}")


import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the password Generator!")
noOfLetters = int(input("How many letters would you like in your pasword?"))
noOfSymbols = int(input("How many Symbols would you like?"))
noOfNumbers = int(input("How many numbers would you like?"))

password = ""

# low level generater
# for char in range(1, noOfLetters + 1):
#     password += random.choice(letters)

# for char in range(1, noOfSymbols + 1):
#     password += random.choice(symbols)

# for char in range(1, noOfNumbers + 1):
#     password += random.choice(numbers)

#Hard Level
password_list = []

for char in range(1, noOfLetters + 1):
  password_list.append(random.choice(letters))

for char in range(1, noOfSymbols + 1):
  password_list += random.choice(symbols)

for char in range(1, noOfNumbers + 1):
  password_list += random.choice(numbers)

print(password_list)
random.shuffle(password_list)
print(password_list)

password = ""
for char in password_list:
  password += char

print(f"Your password is: {password}")