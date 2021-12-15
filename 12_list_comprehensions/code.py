#normal way to doubled the numbers
numbers = [1,3,5]
doubled = []

for num in numbers:
    doubled.append(num*2)
print(doubled)

# list comp
numbers = [1,3,5]
doubled = [num*2 for num in numbers]
print(doubled)

# dealing with strings normal method
friends = ["rolf", "sam", "jen", "ren", "ken"]
start_s = []

for friend in friends:
    if friend.startswith("s"):
        start_s.append(friend)
print(start_s)


# dealing with strings via list comp
friends = ["rolf", "sam", "jen", "ren", "ken"]
start_s = [friend for friend in friends if friend.startswith("s")]


print(start_s)

# list comp creates a new list
friends = ["sam","samantha", "saurabh"]
start_s = [friend for friend in friends if friend.startswith("s")]

print(friends)
print(start_s)
print(friends is start_s)

print("friends: ", id(friends), "start_s: ", id(start_s))