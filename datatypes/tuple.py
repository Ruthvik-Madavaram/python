empty = ()
single_item_tuple = (1, )
fruits = ("apple", "banana", "orange")
subset = fruits[1:3]

count = fruits.count("banana")
print(count)

def get_info():
    return "Ruthvik", 23, "Hyderabad"

for fruit in fruits:
    print(fruit)

name, age, city = get_info()
print(name, age, city)
