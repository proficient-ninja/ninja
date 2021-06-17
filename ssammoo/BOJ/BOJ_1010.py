import sys

repeat_num = int(sys.stdin.readline())

def factorial (n) :
    if n <= 1 :
        return 1
    return n * factorial(n - 1)

for each in range(repeat_num):
    N, M = map(int, sys.stdin.readline().split())
    bridge_num = factorial(M) / (factorial(N) * factorial(M-N))

    print(int(bridge_num))