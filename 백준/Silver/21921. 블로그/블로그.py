# main
n, x = map(int, input().split())
visitor = list(map(int, input().split()))

sum_visitor = [0] * (n + 1)
sum_visitor[1] = visitor[0]

for i in range(2, n + 1):
    sum_visitor[i] = sum_visitor[i - 1] + visitor[i - 1]

max_visitor = 0
max_visitor_cnt = 0

for i in range(x, n + 1):
    curr_visitor = sum_visitor[i] - sum_visitor[i - x]

    if curr_visitor > max_visitor:
        max_visitor = curr_visitor
        max_visitor_cnt = 1
    elif curr_visitor == max_visitor:
        max_visitor_cnt += 1

if max_visitor == 0:
    print("SAD")
else:
    print(max_visitor)
    print(max_visitor_cnt)
