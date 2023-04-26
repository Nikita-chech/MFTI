from random import *

def generate_password():
    s = randint(7, 10)
    l = ''
    for i in range(s):
        g = randint(33, 126)
        l = l + chr(g)
    return l
print(f())