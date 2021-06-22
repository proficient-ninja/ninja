import sys
import heapq

N = int(input())

heap = []

for each in range(N) :
    input_val = int(sys.stdin.readline())
    if input_val == 0 :
        if len(heap) != 0 :
            print(-(heapq.heappop(heap)))
        else :
            print(0)
    else :
        heapq.heappush(heap, -input_val)
