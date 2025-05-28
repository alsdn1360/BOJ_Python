# main
p, m = map(int, input().split())

rooms = []

for _ in range(p):
    l, n = input().split()
    l = int(l)

    if not rooms:
        rooms.append([(l, n)])
    else:
        is_in = False

        for room in rooms:
            if room[0][0] - 10 <= l <= room[0][0] + 10 and len(room) < m:
                room.append((l, n))
                is_in = True
                break

        if not is_in:
            rooms.append([(l, n)])

for room in rooms:
    if len(room) == m:
        print("Started!")
    else:
        print("Waiting!")

    room.sort(key=lambda x: x[1])

    for player in room:
        print(*player)
