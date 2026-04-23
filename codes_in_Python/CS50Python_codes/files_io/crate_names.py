name = input("What's your name? ")


# Not so good way to do it:

# file = open("cs50-names.txt", "a")
# file.write(f"{name}\n")
# file.close()   ----> The disadvantage is that you gotta close the file explicitly


# Better way to do it:
with open("cs50-names.txt", "a") as file:
    file.write(f"{name}\n") # ----> Automatically closes the file when the scope ends