def check_area(xa, ya, xb, yb, xc, yc):
    return abs(xa * (yb - yc) + xb * (yc - ya) + xc * (ya - yb)) / 2


# main
xy = [list(map(int, input().split())) for _ in range(3)]
N = int(input())
trees = [list(map(int, input().split())) for _ in range(N)]

xa, ya = xy[0]
xb, yb = xy[1]
xc, yc = xy[2]

total_area = check_area(xa, ya, xb, yb, xc, yc)

tree_cnt = 0

for x, y in trees:
    area1 = check_area(x, y, xb, yb, xc, yc)
    area2 = check_area(xa, ya, x, y, xc, yc)
    area3 = check_area(xa, ya, xb, yb, x, y)

    if area1 + area2 + area3 == total_area:
        tree_cnt += 1

print(total_area)
print(tree_cnt)
