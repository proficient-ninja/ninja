import sys

how_many = int(sys.stdin.readline())

def gcd(a, b):
    mod = a % b
    while mod > 0 :
        a = b
        b = mod
        mod = a % b
    return b

def lcm(a, b):
    return a * b // gcd(a, b)

for each in range(how_many) :
    a, b = map(int, sys.stdin.readline().split())
    print(lcm(a, b))

""" import sys

how_many = int(sys.stdin.readline())

def make_multiple_arr(num) :
    multiple_arr = []
    for each in range(1,num + 1) :
        if num % each == 0 :
            multiple_arr.append(each)
    return multiple_arr

for each in range(how_many) :
    a, b = map(int, sys.stdin.readline().split())
    left_multiple = set(make_multiple_arr(a))
    right_multiple = set(make_multiple_arr(b))

    equal_multiple_arr = list(left_multiple & right_multiple)
    equal_multiple_arr.sort()
    equal_multiple = equal_multiple_arr[-1]
    min_multiple = int(a * b / equal_multiple)

    print(min_multiple) """