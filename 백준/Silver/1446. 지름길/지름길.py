# main
n, d = map(int, input().split())

dist = [i for i in range(d + 1)]
short_dist = []

for _ in range(n):
    start, end, short_cut = map(int, input().split())

    if (end - start) >= short_cut and end <= d:
        short_dist.append((start, end, short_cut))

for i in range(d):
    dist[i + 1] = min(dist[i + 1], dist[i] + 1)

    for start, end, short_cut in short_dist:
        if i == start:
            dist[end] = min(dist[end], dist[start] + short_cut)

print(dist[d])
