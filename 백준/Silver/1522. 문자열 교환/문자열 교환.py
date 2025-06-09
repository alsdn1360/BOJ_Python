# main
ab = input()

n = len(ab)
window_size = ab.count("a")

extended_ab = ab + ab  # 원형으로 되어있기 때문에 뒤에 한번 더해줌

answer = float("inf")

for i in range(n):
    # 윈도우 안에서 b의 개수만 구해주면 a는 모두 연속으로 이어짐
    # 이때의 b의 개수의 최소값을 구하면 됨
    answer = min(answer, extended_ab[i : i + window_size].count("b"))

print(answer)
