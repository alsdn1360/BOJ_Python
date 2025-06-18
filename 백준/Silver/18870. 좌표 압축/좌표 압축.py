from collections import defaultdict

# main
N = int(input())
coor = list(map(int, input().split()))

comp_coor = sorted(list(set(coor)))  # 해당 숫자보다 작은 숫자의 갯수를 알기위한 리스트
comp_coor_dict = defaultdict(int)  # 원래 숫자와 압축된 숫자를 매칭하는 딕셔너리

# 압축된 숫자의 인덱스는 압축된 숫자 그 자체임(자기보다 더 작은 숫자의 갯수가 압축된 숫자임)
for i, c_c in enumerate(comp_coor):
    comp_coor_dict[c_c] = i

answer = []

for c in coor:
    answer.append(comp_coor_dict[c])

print(*answer)
