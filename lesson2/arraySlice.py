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


print(bounce[0] + ' ' + '[:-3]' +  ' ' + 'First slice of the string UNCOPYRIGHTABLE')
print(bounce[:0] + ' ' + '[:-3]' +  ' ' + 'First slice of the string UNCOPYRIGHTABLE')
print(bounce[0:] + ' ' + '[:-3]' +  ' ' + 'First slice of the string UNCOPYRIGHTABLE')
print(bounce[1]+ ' ' + '[1]' + ' ' + 'Second slice of the string UNCOPYRIGHTABLE')
print(bounce[1:]+ ' ' + '[1:]' + ' ' + 'Second slice to the end of the string UNCOPYRIGHTABLE')
print(bounce[:1]+ ' ' + '[:1]' + ' ' + 'Second slice of the string UNCOPYRIGHTABLE')
print(bounce[-1]+ ' ' + '[-1]' + ' ' + 'Second slice of the string UNCOPYRIGHTABLE')
print(bounce[:-1]+ ' ' + '[:-1]' + ' ' + 'Second slice of the string UNCOPYRIGHTABLE')
print(bounce[-1:]+ ' ' + '[-1:]' + ' ' + 'Second slice of the string UNCOPYRIGHTABLE')
print(bounce[2]+ ' ' + '[2]' + ' ' + 'Third slice of the string UNCOPYRIGHTABLE')
print(bounce[2:]+ ' ' + '[2:]' + ' ' + 'Third slice of the string UNCOPYRIGHTABLE')
print(bounce[:2]+ ' ' + '[:2]' + ' ' + 'Third slice of the string UNCOPYRIGHTABLE')
print(bounce[-2]+ ' ' + '[-2]' + ' ' + 'Third slice of the string UNCOPYRIGHTABLE')
print(bounce[:-2]+ ' ' + '[:-2]' + ' ' + 'Third slice of the string UNCOPYRIGHTABLE')
print(bounce[-2:]+ ' ' + '[-2:]' + ' ' + 'Third slice of the string UNCOPYRIGHTABLE')
print(bounce[3]+ ' ' + '[3]' + ' ' + 'Fourth slice of the string UNCOPYRIGHTABLE')
print(bounce[3:]+ ' ' + '[3]' + ' ' + 'Fourth slice of the string UNCOPYRIGHTABLE')
print(bounce[:3]+ ' ' + '[3]' + ' ' + 'Fourth slice of the string UNCOPYRIGHTABLE')
print(bounce[-3]+ ' ' + '[3]' + ' ' + 'Fourth slice of the string UNCOPYRIGHTABLE')
print(bounce[-3:]+ ' ' + '[-3:]' +  ' '  + 'Fourth slice of the string UNCOPYRIGHTABLE')
print(bounce[:-3]+ ' ' + '[:-3]' +  ' ' + 'Fourth slice of the string UNCOPYRIGHTABLE')
print(bounce[4] + ' ' + '[:-4]' +  ' ' + 'First slice of the string UNCOPYRIGHTABLE')
print(bounce[:4] + ' ' + '[:-4]' +  ' ' + 'First slice of the string UNCOPYRIGHTABLE')
print(bounce[4:] + ' ' + '[:-4]' +  ' ' + 'First slice of the string UNCOPYRIGHTABLE')
print(bounce[-4]+ ' ' + '[-4]' + ' ' + 'Second slice of the string UNCOPYRIGHTABLE')
print(bounce[:-4]+ ' ' + '[:-4]' + ' ' + 'Second slice of the string UNCOPYRIGHTABLE')
print(bounce[-4:]+ ' ' + '[-4:]' + ' ' + 'Second slice of the string UNCOPYRIGHTABLE')
print(bounce[5]+ ' ' + '[5]' + ' ' + 'Third slice of the string UNCOPYRIGHTABLE')
print(bounce[5:]+ ' ' + '[5:]' + ' ' + 'Third slice of the string UNCOPYRIGHTABLE')
print(bounce[:5]+ ' ' + '[:5]' + ' ' + 'Third slice of the string UNCOPYRIGHTABLE')
print(bounce[-5]+ ' ' + '[-5]' + ' ' + 'Third slice of the string UNCOPYRIGHTABLE')
print(bounce[:-5]+ ' ' + '[:-5]' + ' ' + 'Third slice of the string UNCOPYRIGHTABLE')
print(bounce[-5:]+ ' ' + '[-5:]' + ' ' + 'Third slice of the string UNCOPYRIGHTABLE')
print(bounce[6]+ ' ' + '[6]' + ' ' + 'Second slice of the string UNCOPYRIGHTABLE')
print(bounce[6:]+ ' ' + '[6:]' + ' ' + 'Second slice to the end of the string UNCOPYRIGHTABLE')
print(bounce[:6]+ ' ' + '[:6]' + ' ' + 'Second slice of the string UNCOPYRIGHTABLE')
print(bounce[-6]+ ' ' + '[-6]' + ' ' + 'Second slice of the string UNCOPYRIGHTABLE')
print(bounce[:-6]+ ' ' + '[:-6]' + ' ' + 'Second slice of the string UNCOPYRIGHTABLE')
print(bounce[-6:]+ ' ' + '[-6:]' + ' ' + 'Second slice of the string UNCOPYRIGHTABLE')
print(bounce[7]+ ' ' + '[7]' + ' ' + 'Second slice of the string UNCOPYRIGHTABLE')
print(bounce[7:]+ ' ' + '[7:]' + ' ' + 'Second slice to the end of the string UNCOPYRIGHTABLE')
print(bounce[:7]+ ' ' + '[:7]' + ' ' + 'Second slice of the string UNCOPYRIGHTABLE')
print(bounce[-7]+ ' ' + '[-7]' + ' ' + 'Second slice of the string UNCOPYRIGHTABLE')
print(bounce[:-7]+ ' ' + '[:-7]' + ' ' + 'Second slice of the string UNCOPYRIGHTABLE')
print(bounce[-7:]+ ' ' + '[-7:]' + ' ' + 'Second slice of the string UNCOPYRIGHTABLE')
print(bounce[8]+ ' ' + '[8]' + ' ' + 'Second slice of the string UNCOPYRIGHTABLE')
print(bounce[8:]+ ' ' + '[8:]' + ' ' + 'Second slice to the end of the string UNCOPYRIGHTABLE')
print(bounce[:8]+ ' ' + '[:8]' + ' ' + 'Second slice of the string UNCOPYRIGHTABLE')
print(bounce[-8]+ ' ' + '[-8]' + ' ' + 'Second slice of the string UNCOPYRIGHTABLE')
print(bounce[:-8]+ ' ' + '[:-8]' + ' ' + 'Second slice of the string UNCOPYRIGHTABLE')
print(bounce[-8:]+ ' ' + '[-8:]' + ' ' + 'Second slice of the string UNCOPYRIGHTABLE')
print(bounce[9]+ ' ' + '[9]' + ' ' + 'Second slice of the string UNCOPYRIGHTABLE')
print(bounce[9:]+ ' ' + '[9:]' + ' ' + 'Second slice to the end of the string UNCOPYRIGHTABLE')
print(bounce[:9]+ ' ' + '[:9]' + ' ' + 'Second slice of the string UNCOPYRIGHTABLE')
print(bounce[-9]+ ' ' + '[-9]' + ' ' + 'Second slice of the string UNCOPYRIGHTABLE')
print(bounce[:-9]+ ' ' + '[:-9]' + ' ' + 'Second slice of the string UNCOPYRIGHTABLE')
print(bounce[-9:]+ ' ' + '[-9:]' + ' ' + 'Second slice of the string UNCOPYRIGHTABLE')
print(bounce[10]+ ' ' + '[10]' + ' ' + 'Second slice of the string UNCOPYRIGHTABLE')
print(bounce[10:]+ ' ' + '[10:]' + ' ' + 'Second slice to the end of the string UNCOPYRIGHTABLE')
print(bounce[:10]+ ' ' + '[:10]' + ' ' + 'Second slice of the string UNCOPYRIGHTABLE')
print(bounce[-10]+ ' ' + '[-10]' + ' ' + 'Second slice of the string UNCOPYRIGHTABLE')
print(bounce[:-10]+ ' ' + '[:-10]' + ' ' + 'Second slice of the string UNCOPYRIGHTABLE')
print(bounce[-10:]+ ' ' + '[-10:]' + ' ' + 'Second slice of the string UNCOPYRIGHTABLE')
print(bounce[11]+ ' ' + '[11]' + ' ' + 'Second slice of the string UNCOPYRIGHTABLE')
print(bounce[11:]+ ' ' + '[11:]' + ' ' + 'Second slice to the end of the string UNCOPYRIGHTABLE')
print(bounce[:11]+ ' ' + '[:11]' + ' ' + 'Second slice of the string UNCOPYRIGHTABLE')
print(bounce[-11]+ ' ' + '[-11]' + ' ' + 'Second slice of the string UNCOPYRIGHTABLE')
print(bounce[:-11]+ ' ' + '[:-11]' + ' ' + 'Second slice of the string UNCOPYRIGHTABLE')
print(bounce[-11:]+ ' ' + '[-11:]' + ' ' + 'Second slice of the string UNCOPYRIGHTABLE')
print(bounce[12]+ ' ' + '[12]' + ' ' + 'Second slice of the string UNCOPYRIGHTABLE')
print(bounce[12:]+ ' ' + '[12:]' + ' ' + 'Second slice to the end of the string UNCOPYRIGHTABLE')
print(bounce[:12]+ ' ' + '[:12]' + ' ' + 'Second slice of the string UNCOPYRIGHTABLE')
print(bounce[-12]+ ' ' + '[-12]' + ' ' + 'Second slice of the string UNCOPYRIGHTABLE')
print(bounce[:-12]+ ' ' + '[:-12]' + ' ' + 'Second slice of the string UNCOPYRIGHTABLE')
print(bounce[-12:]+ ' ' + '[-12:]' + ' ' + 'Second slice of the string UNCOPYRIGHTABLE')
print(bounce[13]+ ' ' + '[13]' + ' ' + 'Second slice of the string UNCOPYRIGHTABLE')
print(bounce[13:]+ ' ' + '[13:]' + ' ' + 'Second slice to the end of the string UNCOPYRIGHTABLE')
print(bounce[:13]+ ' ' + '[:13]' + ' ' + 'Second slice of the string UNCOPYRIGHTABLE')
print(bounce[-13]+ ' ' + '[-13]' + ' ' + 'Second slice of the string UNCOPYRIGHTABLE')
print(bounce[:-13]+ ' ' + '[:-13]' + ' ' + 'Second slice of the string UNCOPYRIGHTABLE')
print(bounce[-13:]+ ' ' + '[-13:]' + ' ' + 'Second slice of the string UNCOPYRIGHTABLE')
print(bounce[14]+ ' ' + '[14]' + ' ' + 'Second slice of the string UNCOPYRIGHTABLE')
print(bounce[14:]+ ' ' + '[14:]' + ' ' + 'Second slice to the end of the string UNCOPYRIGHTABLE')
print(bounce[:14]+ ' ' + '[:14]' + ' ' + 'Second slice of the string UNCOPYRIGHTABLE')
print(bounce[-14]+ ' ' + '[-14]' + ' ' + 'Second slice of the string UNCOPYRIGHTABLE')
print(bounce[:-14]+ ' ' + '[:-14]' + ' ' + 'Second slice of the string UNCOPYRIGHTABLE')
print(bounce[-14:]+ ' ' + '[-14:]' + ' ' + 'Second slice of the string UNCOPYRIGHTABLE')

# slicing with strides on the latter part

print(bounce[1:4:2]+ ' ' + '[1:4:2]' + ' ' + 'Second slice of the string to the fourth slice, then delete from the fourth to the second string UNCOPYRIGHTABLE')
print(bounce[2:14:5]+ ' ' + '[2:14:5]' + ' ' + 'Third slice of the string UNCOPYRIGHTABLE')
print(bounce[4:14:4]+ ' ' + '[4:14:4]' + ' ' + 'Second slice of the string UNCOPYRIGHTABLE')
print(bounce[:14:6]+ ' ' + '[:14:6]' + ' ' + 'Second slice of the string UNCOPYRIGHTABLE')
print(bounce[4::2]+ ' ' + '[4::2]' + ' ' + 'Second slice of the string UNCOPYRIGHTABLE')




print(len(bounce))

n = int(input("type in an integer ---->   "))
print(n)
print(type(n))
