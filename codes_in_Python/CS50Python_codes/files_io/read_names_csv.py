names = []

with open("cs50-names.csv", "r") as file:
    for line in file:
        name, gender = line.rstrip().split(",")
        print(f"{name} is a {gender}")