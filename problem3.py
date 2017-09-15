
# Project Euler - Problem 3

# The prime factors of 13195 are 5, 7, 13 and 29
# What is the largest prime factor of the number 600851475143?

# 1st attempt

number = 13195
number = 600851475143

for x in xrange(2,number):
    if number % x == 0:
        prime = True
        for y in xrange(2,x):
            if x % y == 0:
                prime = False
                break
        if prime:
            print x

# Answer is 6857
