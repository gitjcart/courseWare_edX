# t.py
"""
varA = '1'
varB = 1
thanks = "We appreciate your interest in our products."
if type(varA) == type('s') or type(varB) == type('s'):
    print("string involved")
elif varA > varB:
    print("bigger")
elif varA == varB:
    print("equal")
elif varA < varB:
    print("smaller")

answer = input('Are you alive? ---> ')
if answer in ['y', 'Y', 'yes', 'Yes', 'YES']:
	print(thanks)
else:
	print('We regretfully aceept your decision for other products.')
print(type('s'))

num = 0
while num <= 5:
    print(num)
    num += 1

print("Outside of loop")
print(num) 

numberOfLoops = 0
numberOfApples = 2
while numberOfLoops < 10:
    numberOfApples *= 2
    numberOfApples += numberOfLoops
    numberOfLoops -= 1
print("Number of apples: " + str(numberOfApples))

num = 10
while num > 3:
    num -= 1
    print(num)
"""


while:
	end = 6
	a = 1
	for x in range(1, end):
		a += x
		print(a)
		if a == 6:
			break