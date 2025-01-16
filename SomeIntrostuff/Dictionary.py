#di= a col of }key:val} pair ordered and changeable no dups

capitals = {"USA": "Washington DC ",
            "India": "New Delhi",
            "China": "Beijing",
            "Russia": "Moscow"}

print(capitals.get("USA"))
print(capitals.get("Canada"))


if capitals.get("Russia"):
    print("that cap exists")
else:
    print("cap doesnt exist")

capitals.update({"Germany":"Berlin"})
#capitals.update({"USA":"Chicago"})
#capitals.pop("China")
#capitals.popitem()
#capitals.clear()

keys= capitals.keys()
print(keys)
for key in capitals.keys():
    print(keys)

values=capitals.values()
print(values)

for value in capitals.values():
    print(value)


items = capitals.items
print(items)

for key,value in capitals.items():
    print(f"{key}:{value}")