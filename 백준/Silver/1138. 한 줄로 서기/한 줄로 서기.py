# main
n = int(input())
taller_mem = list(map(int, input().split()))

line = [float("inf")] * n

for i in range(n):
    curr_person = i + 1
    ramain_taller = taller_mem[i]

    for j in range(n):
        if line[j] > curr_person:
            if ramain_taller > 0:
                ramain_taller -= 1
            else:
                line[j] = curr_person
                break

print(*line)
