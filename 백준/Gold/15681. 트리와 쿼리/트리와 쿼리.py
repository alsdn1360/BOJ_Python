from collections import defaultdict
import sys

sys.setrecursionlimit(10**9)

input = sys.stdin.readline


def make_tree(curr_node, parent):
    for adj_node in edges[curr_node]:
        if adj_node != parent:
            tree[curr_node].append(adj_node)
            make_tree(adj_node, curr_node)


def count_sub_tree_size(curr_node):
    for adj_node in tree[curr_node]:
        count_sub_tree_size(adj_node)
        sub_tree_size[curr_node] += sub_tree_size[adj_node]


# main
n, r, q = map(int, input().split())

edges = defaultdict(list)

for _ in range(n - 1):
    u, v = map(int, input().split())

    edges[u].append(v)
    edges[v].append(u)

tree = defaultdict(list)
make_tree(r, -1)

sub_tree_size = [1] * (n + 1)
count_sub_tree_size(r)

for _ in range(q):
    u = int(input())

    print(sub_tree_size[u])
