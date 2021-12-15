movies_watched = {"watcher", "matrix","saw"}
user_movie = input("enter movie name watched recently: " )

if user_movie in movies_watched:
    print(f"good choice {user_movie} ")
else:
    print(f"I have not watched {user_movie} ")

# number app
number =20
user_input = input("Enter 'y' if you want to play: ").lower()

if user_input == 'y':
    user_number = int(input("guess your number: "))
    if user_number == number:
        print("you are right")
    else:
        print("sorry you are wrong")
else:
    print("no problem if you are not interested to play tha game")


# number app witn in keyword
number =20
user_input = input("Enter 'y' if you want to play: ")

if user_input in ('y', 'Y'):
    user_number = int(input("guess your number: "))
    if user_number == number:
        print("you are right")
    else:
        print("sorry you are wrong")
else:
    print("no problem if you are not interested to play tha game")


# give a hint to user how far he is from the number

number =20
user_input = input("Enter 'y' if you want to play: ").lower()

if user_input == 'y':

    user_number = int(input("guess your number: "))
    if user_number == number:
        print("you are right")

    elif number - user_number in (1, -1):
        print("you are close but off by one")
    
    else:
        print("sorry you are wrong")
else:
    print("no problem, if you are not interested to play tha game")


# using absolute value


number =20
user_input = input("Enter 'y' if you want to play: ").lower()

if user_input == 'y':

    user_number = int(input("guess your number: "))
    if user_number == number:
        print("you are right")

    elif abs (number - user_number) ==1:
        print("you are close but off by one")
    
    else:
        print("sorry you are wrong")
else:
    print("no problem, if you are not interested to play tha game")