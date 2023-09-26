age = int(input("Enter your age: "))
while True:
    if age > 18:
        break
    else:
        age = int(input("Please enter valid age to vote: "))

flag = 5
for i in range(10):
    if i == flag:
        break
    else:
        print(i)
else:
    print("Inside else") # will not execute because the loop is broken at i = 5