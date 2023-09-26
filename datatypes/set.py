empty_set = set()
fruits = {"apple", "banana", "orange"}

fruits.add("cherry")
print(fruits)

fruits.remove("banana")
print(fruits)

set1 = {1,2,3}
set2 = {3,4,5}

intersection_set = set1.intersection(set2)
difference_set = set1.difference(set2)
symmetric_diff_set = set1.symmetric_difference(set2)
print(intersection_set, difference_set, symmetric_diff_set)

if "banana" in fruits:
    print("found!")
else:
    print("not found")

fruits_copy = fruits.copy()
print(fruits_copy)

fruits.clear()
print(fruits)

squares = { x**2 for x in range(10) }