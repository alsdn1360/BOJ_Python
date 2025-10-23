# main
n = int(input())
coeffs = list(map(int, input().split()))

answer = 0

# 시작: 최고차항 계수 a_N(coeffs[0])은 항상 1
# 'x' 버튼 1번 (값: x)
answer += 1

for i in range(1, n + 1):
    coeff = coeffs[i]  # 현재 처리할 계수

    # 계수 더하기
    # 계수가 0보다 큰 경우에만 '+' 및 숫자를 누름
    if coeff > 0:
        # '+' 버튼 1회
        answer += 1
        # 숫자 버튼 (계수의 자릿수만큼)
        answer += len(str(coeff))

    # 'x' 곱하기
    # 마지막 항(상수항, i=n)을 더한 후에는 'x'를 곱하지 않음
    if i < n:
        # '*' 버튼 1회
        answer += 1
        # 'x' 버튼 1회
        answer += 1

# 마지막 '=' 버튼
answer += 1

print(answer)
