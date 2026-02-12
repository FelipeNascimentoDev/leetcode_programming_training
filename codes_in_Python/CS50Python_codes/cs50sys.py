import sys


def version_1():
    try:
        print("hello, my name is " + sys.argv[1])
    except IndexError:
        print("Too few arguments! ")


def version_2():
    if len(sys.argv) < 2: #sys.args counts the first "element" as the name of the program, so its "default is 1". Eg. on the terminal --> python.py
        print("Way too few arguments! ")
    elif len(sys.argv) > 2:
        print("Way too much arguments! ")
    else:
        print("hello, my name is " + sys.argv[1])



def version_3():
    if len(sys.argv) < 2:
        sys.exit("Way too few arguments! ")
    elif len(sys.argv) > 2:
        sys.exit("Way too much arguments! ")
    print("hello, my name is " + sys.argv[1])


#   -----   -----   -----   -----   -----   -----   -----   -----   -----   -----   -----   -----   -----   -----   -----
# From now on it will acept more then 2 argument on the terminal (that's to say, more then "python cs50sys.py Name"):
#   -----   -----   -----   -----   -----   -----   -----   -----   -----   -----   -----   -----   -----   -----   -----


def version_4(): #Print the full list with all the "elements" 
    if len(sys.argv) < 2:
        sys.exit("Way too few arguments! ")
    for arg in sys.argv: # Here is saying "all the args"
        print("hello, my name is " + arg)



def version_5(): # #Print a "SLICE" of the list
    if len(sys.argv) < 2:
        sys.exit("Way too few arguments! ")
    for arg in sys.argv[1:]: # Here is saying "all the args", above the position 1, by using --> [1:]
        print("hello, my name is " + arg)



#   -----   -----   -----   -----   -----   -----   -----   -----   -----   -----   -----   -----   -----   -----   -----
# version_wanted-version()
version_5()