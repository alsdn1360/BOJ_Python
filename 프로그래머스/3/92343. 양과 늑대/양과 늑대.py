from collections import defaultdict
from collections import deque

# 양과 늑대 트리 생성 함수
def build_tree(edges):
    tree = defaultdict(list)

    # 부모 노드와 자식 노드를 key, value로 딕셔너리 생성
    for parent, child in edges:
        tree[parent].append(child)
        
    return tree

def solution(info, edges):
    tree = build_tree(edges)
    max_sheep_cnt = 0
    
    # BFS를 위한 큐 생성
    # (현재 위치, 양의 수, 늑대의 수, 방문한 노드 집합)
    queue = deque([(0, 1, 0, set())])
    
    while queue:
        current_node, sheep_cnt, wolf_cnt, visited = queue.popleft()
        
        # 최대 양의 수 갱신
        max_sheep_cnt = max(sheep_cnt, max_sheep_cnt)
        
        # 인접한 노드 추가
        visited.update(tree[current_node])
        
        for next_node in visited:
            # 다음 노드가 늑대일 때
            if info[next_node]:
                # 늑대의 수보다 양의 수가 더 많아야 하는 조건
                if sheep_cnt > wolf_cnt + 1:
                    queue.append((next_node, sheep_cnt, wolf_cnt + 1, visited - {next_node}))
                    
            # 다음 노드가 양일 때
            else:
                queue.append((next_node, sheep_cnt + 1, wolf_cnt, visited - {next_node}))
    
    return max_sheep_cnt