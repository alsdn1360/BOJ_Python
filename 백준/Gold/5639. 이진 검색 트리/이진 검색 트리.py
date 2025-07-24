import sys

sys.setrecursionlimit(10**6)

input = sys.stdin.readline


def get_postorder(start, end):
    if start > end:
        return

    root = preorder[start] # root는 항상 첫번째 값

    mid = end + 1 # 오른쪽 서브트리가 없을 수도 있기 때문에 +1 해줌

    # 오른쪽 서브트리의 시작점(mid)을 찾기위한 반복문(root보다 큰 수들)
    for i in range(start + 1, end + 1):
        if preorder[i] > root:
            mid = i
            break

    get_postorder(start + 1, mid - 1) # 왼쪽 서브트리 재귀 순회
    get_postorder(mid, end) # 오른쪽 서브트리 재귀 순회
    print(root)


# main
preorder = []

while True:
    try:
        preorder.append(int(input()))
    except:
        break

get_postorder(0, len(preorder) - 1)
