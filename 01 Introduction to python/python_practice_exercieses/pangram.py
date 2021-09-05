"""
Write a function to check whether a string is a pangram or not.
Note : Pangrams are words or sentences containing every letter of the alphabet at least once
"""

from string import ascii_lowercase as asc_lower


# print(asc_lower)
def check(s):
    return set(asc_lower) - set(s.lower()) == set([])


strng = input("Enter string:")
if check(strng):
    print("The string is a pangram")
else:
    print("The string isn't a pangram")



