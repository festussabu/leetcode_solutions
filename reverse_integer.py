def reverse(x):
    if (x == 0):
        return 0
    reversed_string = ''
    negative = x < 0
    x = abs(x)
    for i in reversed(str(x)):
        if i == '0' and not reversed_string:
            continue
        reversed_string += i
    reversed_string = int(reversed_string)
    if (reversed_string > 2**31 - 1) or (reversed_string < -2**31):
        return 0
    if negative:
        reversed_string =  -reversed_string
    return reversed_string

x = 123
# x = 1020
x = 1534236469
print(reverse(x))


'''
Example 1:

Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321
Example 3:

Input: x = 120
Output: 21
'''


# T:O(n)
# S:O(n)
