"""
Write a function that accepts a hyphen-separated sequence of words as input and prints the words in a
 hyphen-separated sequence after sorting them alphabetically
input : green-red-yellow-black-white
output : black-green-red-white-yellow
"""

items = [n for n in input().split('-')]
items.sort()
print('-'.join(items))