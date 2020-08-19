fib = [0,1,1,2,3,5,8,13,21,34,55]
a = list(map(lambda x : True if not x % 2 else False,fib))
print(a)
#result = (list(filter(lambda x: x % 2 != 0, fib)))
#print(result)
#result = (list(filter(lambda x: x % 2 == 0, fib)))
#print(result)