from collections import deque


def bfs(n):
    queue = deque([(n, 0)])
    visited = [False] * (n + 1)
    visited[n] = True

    while queue:
        num, cnt = queue.popleft()

        if num == 1:
            return cnt

        if num % 3 == 0:
            new_num = num // 3

            if not visited[new_num]:
                queue.append((new_num, cnt + 1))
                visited[new_num] = True
        
        if num % 2 == 0:
            new_num = num // 2

            if not visited[new_num]:
                queue.append((new_num, cnt + 1))
                visited[new_num] = True
        
        new_num = num - 1

        if not visited[new_num]:
            queue.append((new_num, cnt + 1))
            visited[new_num] = True


# main
n = int(input())

print(bfs(n))
