# main
remain_n = input()
idx = 0  # 남은 숫자의 인덱스

n = 0

while idx < len(remain_n):
    n += 1

    str_n = str(n)

    for s in str_n:
        if idx < len(remain_n) and s == remain_n[idx]:
            idx += 1

print(n)
