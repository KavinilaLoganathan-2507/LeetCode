# Check Divisibility by digit sum and product

# you are given a positive integer n. Determine whether n is divisible by the sum of the following two values:

# The digit sum of n (the sum of its digits).

# The digit product of n (the product of its digits).

# Return true if n is divisible by this sum; otherwise, return false.

 

# Example 1:

# Input: n = 99

# Output: true

# Explanation:

# Since 99 is divisible by the sum (9 + 9 = 18) plus product (9 * 9 = 81) of its digits (total 99), the output is true.

class Solution:
    def checkDivisibility(self, n):
        sum_digit = 0
        product_digit = 1
        num = n


        while num > 0:
            sum_digit += num % 10
            product_digit *= num % 10
            num //= 10


        return n % (sum_digit + product_digit) == 0
