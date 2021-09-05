"""
Write a python program to make a mark sheet
"""


def stars(n):
    for i in range(n):
        print("*", end='')


def pr(subject, name):
    return print(f"Marks in {subject} = {name}")


phyics = input('Enter Physics Marks : ')
chemistry = input('Enter Chemistry Marks : ')
bio = input('Enter Biology Marks : ')
islamiat = input('Enter Islamiat Marks : ')
urdu = input('Enter Udru Marks : ')
total = int(phyics) + int(chemistry) + int(bio) + int(islamiat) + int(urdu)
percent = (total * 100) / 500

stars(35)
print()
pr('Phyics', phyics)
pr('Chemistry', chemistry)
pr('Biology', bio)
pr('Islamait', islamiat)
pr('Urdu', urdu)
stars(35)
print()
print('Total = ' + str(total))
print('Percentage = ' + str(percent))
