N = int(input())

complex_arr = []

dx = [-1, 0, 1, 0] # 북 동 남 서 순(css 규칙, 시계방향)
dy = [0, 1, 0, -1]

for each in range(N) :
    input_arr = list(input())
    complex_arr.append(input_arr)

count_arr = []

def BFS(x, y) :
    queue = [[x, y]]
    complex_arr[x][y] = "0"
    count = 1

    while queue :
        a, b = queue[0][0], queue[0][1]
        del queue[0]
        for each in range(4):
            i = a + dx[each]
            j = b + dy[each]
            if 0 <= i < N and 0 <= j < N and complex_arr[i][j] == "1" :
                queue.append([i, j])
                complex_arr[i][j] = "0"
                count += 1
    
    count_arr.append(count)

for x in range(N):
    for y in range(N):
        if complex_arr[x][y] == "1" :
            BFS(x, y)

count_arr.sort()

print(len(count_arr))

for each in count_arr :
    print(each)