student_heights = [180, 124, 165, 173, 189, 169, 146]
total = 0

for height in student_heights:
  total += height

print("Average:", total / 7)

# ------------x----------------

student_scores = [78, 65, 89, 86, 55, 91, 64, 89]
highest = 0

for score is student_scores:
  if highest > score:
    hightest == score

pirnt("Highest Score:", highest)

# x 

student_scores = [78, 65, 89, 86, 55, 91, 64, 89]
highest = 0

for score in student_scores:
  if highest < score:
    highest = score

print("Highest Score:", highest)

#------------------x------------

total = 0
for i in range(2, 101, 2):
  total += i
print("Total:", total)

#----------------x----------------

import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

password = ""

for _ in range(4):
  password += random.choice(letters)

for _ in range(2):
  password += random.choice(symbols)

for _ in range(2):
  password += random.choice(numbers)

print(password)

# String Concat
greeting = "Hello "
greeting += "World"
print(greeting)

# Random
import random

fruits = ['apple', 'banana', 'watermelon']
print(random.choice(fruits))

for i in range(4, 15, 2):
  print(i)

# https://docs.google.com/presentation/d/1wckeFIr0GyCy7ugbnNNdMEym_l3TXovCGyg5640oXYw/edit?usp=sharing