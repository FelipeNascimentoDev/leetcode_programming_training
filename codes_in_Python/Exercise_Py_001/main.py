# Python dictionary exercise

G = "Griffindor"
S = "Slytherin"
R = "Ravenclaw"

students = {
    "Hermione": G,
    "Draco": S,
    "Luna": R,
    "Harry": G,
    "Ron": G
}

for student in students:
    print(student, students[student], sep=", ")