def greet():
    print("We are learning functions")

def find_reactangle_area(l, b):
    return l*b

#variable args
def print_squares_of_nums(*nums):
    for num in nums:
        print(num*num)

#default args
def divide(a, b = 7):
    return a / b

greet()
print_squares_of_nums(1,2,3,4)
print(find_reactangle_area(2,3))
print(divide(10,5))
print(divide(21))
print(divide(b = 5, a = 2))