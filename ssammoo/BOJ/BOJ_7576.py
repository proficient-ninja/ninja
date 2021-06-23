import sys
from collections import deque

M, N = map(int, input().split())

graph = []

for each in range(N) :
    graph.append(list(map(int, sys.stdin.readline().split())))

queue = deque()
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

for x in range(N):
    for y in range(M):
        if graph[x][y] == 1:
            queue.append([x, y])

def BFS() :
    while queue :
        x, y = queue.popleft()
        for each in range(4) :
            i = x + dx[each]
            j = y + dy[each]
            if 0 <= i < N and 0 <= j < M and graph[i][j] == 0 :
                graph[i][j] = graph[x][y] + 1
                queue.append([i, j])

BFS()

isTrue = False
result = -2

for x in graph :
    for y in x :
        if y == 0 :
            isTrue = True
        result = max(result, y)

if isTrue == True :
    print(-1)
elif result == 1 :
    print(0)
else :
    print(result - 1)