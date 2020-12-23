"""
Hi, here's your problem today. This problem was recently asked by Facebook:

Kaprekar's Constant is the number 6174. This number is special because it has the property where for any 4-digit number that has 2 or more unique digits, if you repeatedly apply a certain function it always reaches the number 6174.

This certain function is as follows:
- Order the number in ascending form and descending form to create 2 numbers.
- Pad the descending number with zeros until it is 4 digits in length.
- Subtract the ascending number from the descending number.
- Repeat.

Given a number n, find the number of times the function needs to be applied to reach Kaprekar's constant. Here's some starter code:

KAPREKAR_CONSTANT = 6174

def num_kaprekar_iterations(n):
  # Fill this in.

print num_kaprekar_iterations(123)
# 3
# Explanation:
#  3210 - 123 = 3087
#  8730 - 0378 = 8352
#  8532 - 2358 = 6174 (3 iterations)
"""
KAPREKAR_CONSTANT = 6174
# Solution 1
def num_kaprekar_iterations(n, times = 0):
    if n == KAPREKAR_CONSTANT:
        return times
    str_n = str(n)
    str_n = ((4-len(str_n))* "0") + str_n

    asc = "".join(sorted(str_n))
    asc_n = int(asc)
    dec_n = int(asc[::-1])
    return num_kaprekar_iterations(dec_n-asc_n, times+1)


# Solution 2
def num_kaprekar_iterations1(n):
    times = 0
    return recursion(n, times, appeared = set())

def recursion(n, times, appeared):
    if n == KAPREKAR_CONSTANT:
        return times

    digits = []
    while n > 0:
        r = n % 10
        digits.append(r)
        n = n // 10

    while len(digits) < 4:
        digits.append(0)

    asc = int("".join([str(i) for i in sorted(digits)]))
    dec = int("".join([str(i) for i in sorted(digits,reverse=True)]))
    diff = dec - asc

    if diff in appeared:
        return -1

    appeared.add(diff)
    return recursion(diff, times+1, appeared)


print(num_kaprekar_iterations(123))
# 3
# Explanation:
#  3210 - 123 = 3087
#  8730 - 0378 = 8352
#  8532 - 2358 = 6174 (3 iterations)
print(num_kaprekar_iterations(1000))
print(num_kaprekar_iterations(191))
print(num_kaprekar_iterations(6174))
print(num_kaprekar_iterations(788))