n = int(input())

arr = [list(map(int, input().split())) for each in range(n)]

white, blue = 0, 0


def check (x, y, n) :
    paper_color = arr[x][y]
    
    for x_val in range(x, x + n):
        for y_val in range(y, y + n):
            if arr[x_val][y_val] != paper_color:
                return False
    return True

def count_paper(x, y, n) :
    global white, blue

    if check(x, y, n) :
        if arr[x][y] == 1 :
            blue += 1
        else :
            white += 1
    else :
        half = n // 2

        count_paper(x, y, half)
        count_paper(x + half, y , half)
        count_paper(x, y + half, half)
        count_paper(x + half, y + half, half)

count_paper(0,0,n)
print(white)
print(blue)
