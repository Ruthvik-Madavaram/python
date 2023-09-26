string = "example_string"
for char in string:
    print(char)

fruits = ["Oranges", "Bananas", "Apples"]
for fruit in fruits:
    print(fruit)

for i in range(len(fruits)):
    print(fruits[i])

#for-else
#else doesn't execute if the loop is breaked
for i in range(5):
    print("Inside for")
else:
    print("Inside else")