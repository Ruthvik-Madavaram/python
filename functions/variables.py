def add(n1, n2):
    result = n1 + n2 #here result is local var
    print(result)

#print(result) results in error
add(2,3)

message = "global scope"
def greet():
    message = "local scope"
    print("Inside greet: ", message)

greet()
print("global scope: ", message)


res = 0
def sub(n1, n2):
    global res
    res = n1 - n2
sub(2,3)
print(res)

def outer_func():
    num = 20
    def inner_func():
        global num
        num = 30
    print("Before calling inner_func: ", num)
    inner_func()
    print("After calling inner_func: ", num)

outer_func()
print("Global scope: ", num)

z = 10
def outer_func():
    z = 10
    def inner_func(): 
        nonlocal z
        z += 10
    print("Before calling inner_func: ", z)
    inner_func()
    print("After calling inner_func: ", z)

outer_func()
print("Global scope: ", z)