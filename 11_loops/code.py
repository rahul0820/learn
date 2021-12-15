#While Loop

number =20

while True:
    user_input = input("would you like to play? (Y/n) ")

    if user_input == "n":
        break

    user_number = int(input("guess your number: "))
    if user_number == number:
        print("you are right")
    elif number - user_number in (1, -1):
        print("you are close but off by one")
    else:
        print("sorry you are wrong")


# For Loop

friends = ["rolf","jen","chris", "ren"]

for friend in friends:
    print(f"{friend} is my friend.")


# for loop to calculate avg grade

grades = [35,67,98,100,100]
total = 0
amount = len(grades)

for grade in grades:
    total = total+grade
print(total/amount)


#  calculate avg grade without for loop


grades = [35,67,98,100,100]
total = sum(grades)
amount = len(grades)


print(total/amount)