
computer_num = int(input())
connect_num = int(input())

graph = [[0] * (computer_num + 1) for i in range(computer_num + 1)]

for each in range(connect_num):
    val_x, val_y = map(int, input().split())
    graph[val_x][val_y] = 1
    graph[val_y][val_x] = 1

start_computer = 1

def DFS(start_num, graph_arr) :
    stack = [start_num]
    visited = [start_num]

    while stack :
        current_node = stack.pop()
        for graph_node in range(len(graph_arr[current_node])) :
            if graph_arr[current_node][graph_node] == 1 and graph_node not in visited :
                stack.append(graph_node)
                visited.append(graph_node)

    return visited


visited_arr = DFS(start_computer, graph)
print(len(visited_arr) - 1)