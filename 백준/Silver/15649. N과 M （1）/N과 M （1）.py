from itertools import permutations

# main
n, m = map(int, input().split())
arr = [i for i in range(1, n + 1)]

for permu in permutations(arr, m):
    print(*list(permu))
