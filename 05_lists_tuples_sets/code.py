#list - defined by[]
# can add/remove elements
l = ["rahul", "age", "city"]
print(l[1])

#Modify items in list
l[0] = "nation"
print(l)

#add a list by .append()
l.append("nation")
print(l)

#remove element
l.remove("rahul")
print(l)

#tuple - defined by ()
# can't remove/add any element
t = ("rahul", "age", "city")
print(t[0])






# sets - defined by {}
# can add/remove elements but can't have duplicate the elements
s = {"rahul", "age", "city"}

# add to sets
s.add("nation")
print(s)
# Note - lists and tuples always the keeps the order but in terms of sets it is not necessary that will have the same order