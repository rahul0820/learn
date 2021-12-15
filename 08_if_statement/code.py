# it allows us to use a boolean to make a decision in out program and do differnt things depending on the value of that boolean

day_of_week = input("what day of week is it today")


if day_of_week == "Monday":
    print("true")
elif day_of_week == "Tuesday":
    print("success")
else:
    print("false")


# dealing with lower vs upper case problem

day_of_week = input("what day of week is it today").lower()


if day_of_week == "monday":
    print("true")
elif day_of_week == "tuesday":
    print("success")
else:
    print("false")