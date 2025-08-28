import sys

input = sys.stdin.readline


# main
n = int(input())
a = list(map(int, input().split()))

m = int(input())
b = list(map(int, input().split()))

# 공통 숫자 집합
common_elem = set(a) & set(b)

# 공통 숫자가 하나도 없으면 종료
if not common_elem:
    print(0)
    exit()

ans = []

while common_elem:
    max_num = max(common_elem)

    ans.append(max_num)

    # 최댓값 이후의 인덱스
    a_idx = a.index(max_num)
    b_idx = b.index(max_num)

    # 그 인덱스로 수열 업데이트
    a = a[a_idx + 1 :]
    b = b[b_idx + 1 :]

    # 이후의 공통 숫자 업데이트
    common_elem = set(a) & set(b)

print(len(ans))
print(*ans)
