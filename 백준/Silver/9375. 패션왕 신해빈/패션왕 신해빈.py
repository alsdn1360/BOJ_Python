from collections import defaultdict

# main
T = int(input())

for test in range(T):
    n = int(input())
    closet = defaultdict(int)
    answer = 1

    for cloth in range(n):
        name, category = input().split()
        closet[category] += 1

    for cnt in closet.values():
        answer *= cnt + 1

    print(answer - 1)
