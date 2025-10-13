# main
n = int(input())

# 1,000개의 1과 1,000개의 1,000으로 모든 약 요구량 N(최대 100만개)을 만들 수 있음
answer = ([1] * 1000) + ([1000] * 1000)

print(len(answer))
print(*answer)
