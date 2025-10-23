# main
n = int(input())
coeffs = list(map(int, input().split()))

# 최소 횟수 계산
total_presses = 0

# 시작: 최고차항 계수 a_N(coeffs[0])은 항상 1
# 'x' 버튼 1번 (값: x)
total_presses += 1

# N-1차항부터 0차항(상수항)까지 반복
# coeffs[1] = a_{N-1}, ..., coeffs[n] = a_0
for i in range(1, n + 1):
    coeff = coeffs[i] # 현재 처리할 계수

    # 1. 계수 더하기
    # 계수가 0보다 큰 경우에만 '+' 및 숫자를 누름
    if coeff > 0:
        # '+' 버튼 1회
        total_presses += 1
        # 숫자 버튼 (계수의 자릿수만큼)
        total_presses += len(str(coeff))
    
    # 2. 'x' 곱하기
    # 마지막 항(상수항, i=n)을 더한 후에는 'x'를 곱하지 않음
    if i < n:
        # '*' 버튼 1회
        total_presses += 1
        # 'x' 버튼 1회
        total_presses += 1

# 3. 마지막 '=' 버튼
total_presses += 1

# 4. 출력
print(total_presses)