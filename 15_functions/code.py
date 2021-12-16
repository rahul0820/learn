# def user_age_in_seconds():
#     user_age = int(input("enter your age: "))
#     age_in_seconds = user_age *365*24*60*60
#     print(f"your age in seconds is {age_in_seconds}")

# user_age_in_seconds()

#DON'T REUSE NAMES

# def print():
#     print("hello world")

# print()

# friends = ["rolf", "bob"]
# def add_friend():
#     friend_name = input("enter your name")
#     friends = friends+[friend_name]

# add_friend()

# CAN'T CALL A FUNCTION BEFORE DEFINING

def add_friend():
    friends.append("rolf")
friends = []
add_friend()
print(friends)
