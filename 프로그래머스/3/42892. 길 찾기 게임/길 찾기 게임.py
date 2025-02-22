import sys
sys.setrecursionlimit(10000)

# 인덱스 값, x, y 값을 가지고 있는 노드 정의
class Node:
    def __init__(self, index, x, y):
        self.index = index
        self.x = x
        self.y = y
        self.left = None
        self.right = None
        
# 현재 노드를 부모 노드와 비교해서 삽입
def insert(parent, child):
    if child.x < parent.x:
        if parent.left is None:
            parent.left = child
        else:
            # 부모 노드의 왼쪽에 이미 있으므로 그 왼쪽에 있는 노드와 현재 노드를 비교
            # 이동 한다는 뜻
            insert(parent.left, child)
    else:
        if parent.right is None:
            parent.right = child
        else:
            # 부모 노드의 오른쪽에 이미 있으므로 그 오른쪽에 있는 노드와 현재 노드를 비교
            # 이동 한다는 뜻
            insert(parent.right, child)
             
# 트리 구현 함수
def build_tree(nodeinfo):
    # 노드 좌표에 각각의 인덱스 추가 
    nodes = [(i + 1, x, y) for i, (x, y) in enumerate(nodeinfo)]
    
    # y가 가장 큰 값이 루트 노드가 됨
    nodes.sort(key = lambda x : (-x[2], x[1]))
    root = Node(nodes[0][0], nodes[0][1], nodes[0][2])
    
    for index, x, y in nodes[1:]:
        insert(root, Node(index, x, y))

    return root

# 전위 순회
def preorder(node):
    if node is None:
        return []
    
    return [node.index] + preorder(node.left) + preorder(node.right)

# 후위 순회
def postorder(node):
    if node is None:
        return []
    
    return postorder(node.left) + postorder(node.right) + [node.index]

def solution(nodeinfo):
    answer = []
    tree = build_tree(nodeinfo)

    answer.append(preorder(tree))
    answer.append(postorder(tree))
    
    return answer
