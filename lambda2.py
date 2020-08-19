

def f(*args):
    s = 0
    for i in args:
        s+=i
    return s * i
print(f(7,6,32,43,3))