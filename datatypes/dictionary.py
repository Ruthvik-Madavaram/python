empty_dict = {}
info = {"name": "Ruthvik", "age": 23, "city": "Hyderabad"}

print(info["name"], info["city"], info["age"])

age = info.get("age")
print(age)
height = info.get("height", "178cm")
print(height)

keys = info.keys()
print(keys)

values = info.values()
print(values)

items = info.items()
print(items)

info.pop("age")
print(info)

other_info = {"height": "178cm", "weight": "80kgs"}
info.update(other_info)
print(info, len(info))

other_info.clear()
print(other_info)

if "name" in info:
    print(info["name"])
