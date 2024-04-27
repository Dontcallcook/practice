# Create a Python script that asks the user how many Fibonacci numbers to generate and then generates them.
# the next number is found by adding up the two numbers before it (starting with 0 and 1).
# 0 + 1 + 1 + 2 + 3 + 5 + 8 + 13
fib_amount = int(input("How many fibonaccci numbers would you like? "))

fib_list = [0, 1]

index = 1
while index < fib_amount - 1:
    fib_number = fib_list[-1] + fib_list[-2]
    fib_list.append(fib_number)
    index += 1

print(fib_list)