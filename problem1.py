
# Project Euler - Problem 1

# If we list all the natural numbers below 10 that are multiples of 3 or 5,
# we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

# 1st attempt

sumOfNums = 0
for number in xrange(1000):
    if number % 5 == 0 or number % 3 == 0:
        sumOfNums += number

print sumOfNums


# 2nd attempt

numbers = list(xrange(1000))
filtered_numbers = filter(lambda number : number % 5 == 0 or number % 3 == 0, numbers)
print sum(filtered_numbers)

# 3rd attempt

print sum([number for number in list(xrange(1000)) if number % 5 == 0 or number % 3 == 0])



# answer = 233168
