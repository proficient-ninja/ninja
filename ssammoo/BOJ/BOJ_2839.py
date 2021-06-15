input_weight = int(input())

## 설탕봉지 무게는 5, 3

sugar_bags = 0

while input_weight >= 0 :
    if input_weight % 5 == 0 :
        sugar_bags = sugar_bags + input_weight // 5
        print(sugar_bags)
        break
    
    input_weight -= 3
    sugar_bags += 1

    if input_weight < 0 :
        print("-1")
