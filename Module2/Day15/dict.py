conversion = {"a": 1, "b": [2,3,4], "c": 3, "d": 4, "e": 5}
print(conversion)
print(type(conversion["b"]))

menu = {"item1": ["egg", "spam", "bacon"],
           "item2": ["egg", "sausage", "spam"],
           "item3": ["egg", "spam"],
           "item4": ["egg", "bacon", "spam"],
           "litem5": ["egg", "bacon", "sausage", "spam"],
           "item6": ["spam", "bacon", "sausage", "spam"],
           "item7": ["spam", "egg", "spam", "spam", "bacon", "spam"],
           "item8": ["spam", "egg", "sausage", "spam"]}

print(menu["item6"][0])

#print(menu.keys())

keys_ord = list(menu.keys())
print(keys_ord)
sorted_keys = sorted(keys_ord)
print(sorted_keys)

order = "item1"
if menu.get(order, 0) == 0:
    print("{} is not a valid dish. Please try again.".format(order))
else:
    print("{} contains {}".format(order, menu.get(order)))

transportation = {"name": "coconut", "color": "brown"}
print(transportation.items())
transportation.setdefault("received_by", "swallow")
print(transportation.items())
transportation.setdefault("received_by", "found_on_ground")
print(transportation.items())