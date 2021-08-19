"""
Write a program (using functions!) that asks the user for a long string containing multiple words.
Print back to the user the same string, except with the words in backwards order
"""


def reverse_word(string):
    return ' '.join(string.split(' ')[::-1])


print(reverse_word('I live in Pakistan'))