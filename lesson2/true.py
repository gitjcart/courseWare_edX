# true.py
#
while True:
    try:
#
        age = int(input("Please enter your age: "))
    except ValueError:
        print("Please enter valid, positive integers.")
        #better try again... Return to the start of the loop
        continue
#
    else:
        #age was successfully parsed!
        #we're ready to exit the loop.
        break
#
if age >= 18 and age <= 120: 
    print("you're old enough to vote in the United States, congrats on staying alive, Citizen.")
elif age >= 121:
	print("nobody is that old, silly.")
elif age < 7:
	print("come on . . . someone that young needs parental assistance on the internet . . . ")
elif age == 0:
	print("you're a newborn or not alive . . . either way, please try again.")
else:
    print("you cannot partake in the voting festivities . . . patience young padawan, patience . . . ")

# if type(len(name)) == int


"""
while True:
	try:
		name = str(input("What is your name good sir or madam? -- > "))
	except ValueError:
		print("sorry, i didn't catch that..")
		continue
	else:
		break
if len(name) >= 8:
	print(" you , got a long , name buddy.")
elif len(name) < 8 and len(name) > 5:
	print("that's a , normal , length name , guy")
else:
	print("short and sweet : - ) ")
"""

# I want to write a function to perform the actions of a while loop with user input being saved to the variable AGE
# then i want a series of conditional statements to evaluate the age variable. if certain expectations are not met
# then i want to rerun the function for collecting user input. ---> a future endeavor!