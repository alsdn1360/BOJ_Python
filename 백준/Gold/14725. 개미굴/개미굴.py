import sys

sys.setrecursionlimit(10**9)


def dfs(curr_colony, floor):
    sorted_colony_key = sorted(curr_colony.keys())

    for key in sorted_colony_key:
        print(f"{floor * '--'}{key}")

        dfs(curr_colony[key], floor + 1)


# main
N = int(input())

colony = {}

for _ in range(N):
    K = list(input().split())

    t = int(K[0])
    foods = K[1:]

    curr_food = colony

    for food in foods:
        curr_food = curr_food.setdefault(food, {})

dfs(colony, 0)
