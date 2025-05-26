# main
n = int(input())
demand = list(map(int, input().split()))
m = int(input())

if sum(demand) <= m:
    answer = max(demand)
else:
    answer = 0
    left, right = 0, max(demand)

    while left <= right:
        mid = (left + right) // 2

        total = sum([min(d, mid) for d in demand])

        if total <= m:
            answer = mid
            left = mid + 1
        else:
            right = mid - 1

print(answer)
