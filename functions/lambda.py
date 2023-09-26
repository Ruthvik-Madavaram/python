lambda : print("Anonymous functions")

mul = lambda x,y: x*y
print(mul(3,5))

x = [(1,2), (3,5), (7, 0), (3,4)]
x.sort(key= lambda x: x[1], reverse=True)
print(x)