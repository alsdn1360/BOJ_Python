# main
n = int(input())
taller_mem = list(map(int, input().split()))

line = [0] * n

for i in range(n):
    taller_cnt = 0

    for j in range(n):
        if line[j] == 0:
            if taller_cnt == taller_mem[i]:
                line[j] = i + 1
                break

            taller_cnt += 1

print(*line)
