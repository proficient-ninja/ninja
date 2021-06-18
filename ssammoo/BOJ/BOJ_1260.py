total_node, total_line, start_num = map(int,input().split())

graph_matrix = [[0]* (total_node + 1) for each in range(total_node + 1)]

for each in range(total_line) :
    x, y = map(int, input().split())
    graph_matrix[x][y] = 1
    graph_matrix[y][x] = 1

def BFS(start_num, visited) :
    visited.append(start_num)
    
    for node in range(len(graph_matrix[start_num])) :
        if graph_matrix[start_num][node] == 1 and node not in visited :
            BFS(node, visited)

    return visited

def DFS(start_num) :
    queue = [start_num]
    visited = [start_num]

    while queue :
        current_node = queue.pop(0)
        for node in range(len(graph_matrix[start_num])) :
            if graph_matrix[current_node][node] == 1 and node not in visited :
                queue.append(node)
                visited.append(node)
    return visited



print(*BFS(start_num, []))
print(*DFS(start_num))
