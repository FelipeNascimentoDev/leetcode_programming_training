names = []

# EXAMPLE USING ".txt" FILES:
with open("cs50-names.txt", "r") as files: # The default value is "r" so you don't actually need to type "r" everytime
    for line in files:
        names.append(line.rstrip())

for name in sorted(names, reverse=True):
    print(f"Hello, {name}")