# outputting "stuff" to STDOUT

x=1
print(x)
x_str = str(x)
print(x_str)
print("my fav num is", x, ".", "x =", x)
print("my fav num is " + x_str + ". " + "x = " + x_str)
print("my fav num is " + "%s" + "." + "x= " + "%s") %(x_str, x_str)