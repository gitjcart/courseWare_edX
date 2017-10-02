# correctShortcut.py

#!/usr/local/bin/python3

x = "Hello"
print ("Hello World! %s" %(x))



# HERE IS THE WRONG FORMAT. where x is a string. and print() is a NoneType.
# The NoneType doesnt return anything, when it tries to get x for the value None,
# it pulls an error. 


# x = "Hello"
# print ("Hello World! %s") %(x)

# Raises the following error:

# Hello World! %s
# Traceback (most recent call last):
#	 File "main.py", line 3, in 
#	 print ("Hello World! %s") %(x)
# TypeError: unsupported operand type(s) for %: 'NoneType' and 'str'