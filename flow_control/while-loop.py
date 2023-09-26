number = int(input("Enter a number: "))
total  = 0
while number != 0:
    total += number
    print("Type 0 to exit")
    number = int(input("Enter a number: "))
print(total)

#while-else
#else doesn't execute if the loop is breaked
counter = 0
while counter < 3:
    counter += 1
else:
    counter += 100
print(counter)