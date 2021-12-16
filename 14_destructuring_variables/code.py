#DESTRUCTURING IN FOR LOOPS

student_attendance = {"rolf": 96, "bob":80, "anne":100}


for student, attendance in student_attendance.items():
    print(f"{student}: {attendance}")


#ANOTHER EXAMPLE
people = [("bob", 42, "mechanic"), ("james", 24, "atrist"), ("harry", 32, "lecturer")]

for name, age, profession in people:
    print(f"name: {name}, age: {age}, profession: {profession}")

# another example ignoring values
person = ("bob", 42, "mechanic")
name, _, profession = person

print(name, profession)


#COLLECTING VALUES

head, *tail = [1,2,3,4,5]
print(head)
print(tail)