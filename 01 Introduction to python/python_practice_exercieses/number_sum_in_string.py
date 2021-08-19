"""
Given a string, return the sum and average of the digits that appear in the string, ignoring all other characters.
"""


def findSum(str1):
    temp = "0"
    Sum = 0
    count = 0
    for ch in str1:
        if ch.isdigit():
            Sum += int(ch)
            count += 1
    return Sum + int(temp), Sum / count


s, a = findSum('Q-301 is at 4 th floor of quaid block.')

print('Sum')
print(s)
print('Average')
print(a)
