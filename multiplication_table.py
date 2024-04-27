# Write a program that takes a number from the user and prints its multiplication table up to 10.
# For instance, if the user inputs 3, it should print the multiplication table for 3 (from 3x1 to 3x10).

number = int(input("What multiplication table would you like? "))

table = []

for value in range(1, 11):
    print(f"{value} * {number} = {value * number}")
