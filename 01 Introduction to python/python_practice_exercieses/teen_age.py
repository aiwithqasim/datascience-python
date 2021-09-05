""""
Given 3 int values, a b c, return their sum.
However, if any of the values is a teen -- in the range 13..19 inclusive -- then that value counts as 0.
"""


def no_teen_sum(a, b, c):
    return fix_teen(a) + fix_teen(b) + fix_teen(c)


def fix_teen(n):
    if 13 <= n <= 19:
        return 0
    return n


print(no_teen_sum(3, 1, 4))
print(no_teen_sum(21, 1, 2))
print(no_teen_sum(13, 1, 19))
