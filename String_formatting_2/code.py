#f-strings


# static string

name = "rahul"
greetings = "hello, rahul"

print(greetings)

#dynamic

name = "rahul"
greetings = f"hello, {name}"

print(greetings)

# tempalte strings with .format()
name = "rahul"
greetings = "hello, {}"
with_name = greetings.format(name)
with_name_two = greetings.format("eklavya")


print(with_name)
print(with_name_two)

#longer template
longer_phrase = "hello, {}. Today is {}"
formatted = longer_phrase.format("rahul", "monday")
print(formatted)