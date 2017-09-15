
# Project Euler - Problem 4

# A palindromic number reads the same both ways. The largest palindrome made
# from the product of two 2-digit numbers if 9009 = 91 x 99
# Find the largest palindrome made from the product of two 3-digit numbers.

# 1st attempt

palindromes = []

for n in range(999, 0, -1):
    for m in range(999, 0, -1):
        product = n * m
        if (str(product) == str(product)[::-1]):
            palindromes.append(product)

print max(palindromes)

# Answer is 906609
