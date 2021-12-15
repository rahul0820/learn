friends = {"bob", "ren", "anne"}
abroad = {"bob", "anne"}
local_friends = friends.difference(abroad)
print(local_friends)


#union of two sets
local = {"rolf"}
abroad = {"bob", "anne"}
friends = local.union(abroad)
print(friends)

#intersection of two sets

art = {"jen", "rolf","charlie", "bob"}
science = {"bob","jen", "adam", "anne"}
both = art.intersection(science)
print(both)