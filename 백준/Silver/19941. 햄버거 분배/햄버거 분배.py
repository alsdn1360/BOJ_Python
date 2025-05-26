# main
answer = 0

n, k = map(int, input().split())
table = list(input())

for i in range(n):
    if table[i] != "P":
        continue

    for j in range(max(0, i - k), min(n, i + k + 1)):
        if table[j] == "H":
            table[j] = "X"
            answer += 1

            break

print(answer)
