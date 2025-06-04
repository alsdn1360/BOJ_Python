from collections import defaultdict


def bt(idx, point):
    if idx == n:
        return point

    # 현재 과목 선택안했을 때
    result = bt(idx + 1, point)

    c, s, dh = candidates[idx]

    schedules = []
    can_take = True

    for i in range(0, len(dh), 2):
        d = dh[i]
        h = int(dh[i + 1])

        if h in lectures[d]:
            can_take = False
            break

        schedules.append((d, h))

    # 현재 과목 수강할 수 있을 때
    if can_take:
        for d, h in schedules:
            lectures[d].append(h)

        result = max(result, bt(idx + 1, point + c))

        for d, h in schedules:
            lectures[d].remove(h)

    return result


# main
n, m = map(int, input().split())

candidates = []

for _ in range(n):
    c, s, *dh = input().split()
    candidates.append((int(c), int(s), dh))

lectures = defaultdict(list)
point = bt(0, 0)

print("YES" if point >= m else "NO")
