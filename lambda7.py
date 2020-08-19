

b = [1,2,3,4,5,6,7,8,9,10]
f = list(filter(lambda b: b/2 in a, a))
g = list(filter(lambda b: b%2 in a, a))
print(f, g)