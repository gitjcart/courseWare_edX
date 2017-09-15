# there is more than one way to slice an array, 
# These are just examples of slicing
import math

bounce='uncopyrightable'
pounce='far'
mouse='mickey'
house='casita'
man='pendejo'

combo=bounce + ' ' + mouse

print(combo)

"""
If you don’t want characters prefaced by \ to be interpreted as special characters,
you can use raw strings by adding an r before the first quote:
"""
# print('C:\some\name')  # here \n means newline!
# print r('C:\some\name')  # note the r before the quote ## THIS DOESN'T QUITE WORK


print(bounce[1]+ ' ' + '[1]' + ' ' + 'Second slice of the string UNCOPYRIGHTABLE')
print(bounce[1:]+ ' ' + '[1:]' + ' ' + 'Second slice of the string UNCOPYRIGHTABLE')
print(bounce[:1]+ ' ' + '[:1]' + ' ' + 'Second slice of the string UNCOPYRIGHTABLE')
print(bounce[-1]+ ' ' + '[-1]' + ' ' + 'Second slice of the string UNCOPYRIGHTABLE')
print(bounce[:-1]+ ' ' + '[-:1]' + ' ' + 'Second slice of the string UNCOPYRIGHTABLE')
print(bounce[-1:]+ ' ' + '[-1:]' + ' ' + 'Second slice of the string UNCOPYRIGHTABLE')
print(bounce[2]+ ' ' + '[2]' + ' ' + 'Third slice of the string UNCOPYRIGHTABLE')
print(bounce[2:]+ ' ' + '[2:]' + ' ' + 'Third slice of the string UNCOPYRIGHTABLE')
print(bounce[:2]+ ' ' + '[:2]' + ' ' + 'Third slice of the string UNCOPYRIGHTABLE')
print(bounce[-2]+ ' ' + '[-2]' + ' ' + 'Third slice of the string UNCOPYRIGHTABLE')
print(bounce[:-2]+ ' ' + '[:-2]' + ' ' + 'Third slice of the string UNCOPYRIGHTABLE')
print(bounce[-2:]+ ' ' + '[-2:]' + ' ' + 'Third slice of the string UNCOPYRIGHTABLE')
print(bounce[3]+ ' ' + '[3]' + ' ' + 'Fourth slice of the string UNCOPYRIGHTABLE')
print(bounce[-3:]+ ' ' + '[-3:]' +  ' '  + 'Fourth slice of the string UNCOPYRIGHTABLE')
print(bounce[:-3]+ ' ' + '[:-3]' +  ' ' + 'Fourth slice of the string UNCOPYRIGHTABLE')
print(bounce[0] + ' ' + '[:-3]' +  ' ' + 'First slice of the string UNCOPYRIGHTABLE')
print(bounce[:0] + ' ' + '[:-3]' +  ' ' + 'First slice of the string UNCOPYRIGHTABLE')
print(bounce[0:] + ' ' + '[:-3]' +  ' ' + 'First slice of the string UNCOPYRIGHTABLE')
print(bounce[1:4:2])
print(bounce[2:3:1])
print(bounce[4:0:2])
print(bounce[0:3:1])
