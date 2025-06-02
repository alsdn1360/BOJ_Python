# main
n = int(input())
taller_mem = list(map(int, input().split()))

line = [float("inf")] * n

for i, taller in enumerate(taller_mem):
    curr_person = i + 1
    ramain_taller = taller

    for j, pos in enumerate(line):
        if pos > curr_person:
            if ramain_taller > 0:
                ramain_taller -= 1
            else:
                line[j] = curr_person
                break
        else:
            continue

print(*line)
