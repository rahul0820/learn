# dictionary is combination of key and value

friend_ages = {"rolf":24, "adam":30, "anne":27}

print(friend_ages["adam"])

# add new key in existing dictionary

friend_ages = {"rolf":24, "adam":30, "anne":27}

friend_ages["bob"]=20

print(friend_ages)

#change value of existing key in dict

friend_ages = {"rolf":24, "adam":30, "anne":27}

friend_ages["rolf"]=20

print(friend_ages)

#LIST OF DICTIONARIES

friends = [
    {"name": "rolf", "age": 24},
    {"name": "adam", "age":30},
    {"name": "anne", "age": 27}


]

print(friends[1]["name"]) #for accessing particular value for particular key


# ITERATION
student_attendance = {"rolf": 96, "bob":80, "anne":100}

for student in student_attendance:
    print(f"{student}: {student_attendance[student]}")

#BETTER way

student_attendance = {"rolf": 96, "bob":80, "anne":100}

for student, attendance in student_attendance.items():
    print(f"{student}: {attendance}")


# USING IN KEYWORD

student_attendance = {"rolf": 96, "bob":80, "anne":100}

if "bob" in student_attendance:
    print(f"bob: {student_attendance['bob']}")
else:
        print("he is not a student of this class")

# CALCULATE AVG
student_attendance = {"rolf": 96, "bob":80, "anne":100}

attendance_values = student_attendance.values()
print(sum(attendance_values) / len(attendance_values))







