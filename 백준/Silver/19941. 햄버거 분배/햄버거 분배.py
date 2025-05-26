# main
answer = 0

n, k = map(int, input().split())
table = list(input())

p_idx = []

for i, t in enumerate(table):
    if t == "P":
        p_idx.append(i)

for p_i in p_idx:
    for h_i in range(p_i - k, p_i + k + 1):
        if 0 <= h_i < n and table[h_i] == "H":
            table[h_i] = "X"
            answer += 1

            break

print(answer)
