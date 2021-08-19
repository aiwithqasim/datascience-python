"""

"""


def findSum(str1):
    temp = "0"
    sum = 0
    count = 0
    for ch in str1:
        if ch.isdigit():
            temp += ch
        else:
            sum += int(temp)
            temp = "0"
    return sum + int(temp)


findSum('Q-301 is at 4 th floor of quaid block.')
