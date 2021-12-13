# name = input("Enter your name:")
# print(name)

#maths 
size_input = input("how big is your house(in square feet)")
square_feet = int(size_input)
square_meter = square_feet/10.8
# print(square_meter)

print(f"{square_feet} square feet is {square_meter} square meters.")

print(f"{square_feet} square feet is {square_meter: .2f} square meters.") # for getting upto 2 places of decimal
