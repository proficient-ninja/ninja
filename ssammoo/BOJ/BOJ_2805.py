tree, need = map(int, input().split())
tree_forest = list(map(int, input().split()))

start = 1
end = max(tree_forest)

while start <= end :
    mid = (start + end) // 2
    total_meter = sum(i-mid if i > mid else 0 for i in tree_forest)
    if total_meter >= need :
        start = mid + 1
    
    else :
        end = mid - 1

print(end)
