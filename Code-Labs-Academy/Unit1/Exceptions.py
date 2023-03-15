a = 12
s = "hello"
try:
    print(a+s)
except TypeError:
    print( "TypeError : unsupported operand type(s) for + : 'int' and 'str'")
else: #if there is no exception
    print ("The operation has been executed successfully")
