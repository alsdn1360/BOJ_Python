#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1753                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: alsdn1360 <boj.kr/u/alsdn1360>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1753                           #+#        #+#      #+#     #
#    Solved: 2025/02/26 16:51:40 by alsdn1360     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

import heapq, sys

input = sys.stdin.readline

# main
V, E = map(int, input().split())
K = int(input())

graph = [[] for _ in range(V + 1)]
weights = [float("inf")] * (V + 1)

for cnt in range(E):
    u, v, w = map(int, input().split())

    graph[u].append((v, w))
weights[K] = 0

# Dijkstra
heap = []
heapq.heappush(heap, [0, K])

while heap:
    curr_weight, curr_node = heapq.heappop(heap)

    for adj_node, adj_weight in graph[curr_node]:
        weight = curr_weight + adj_weight

        if weight < weights[adj_node]:
            weights[adj_node] = weight
            heapq.heappush(heap, [weight, adj_node])

for i in range(V):
    if weights[i + 1] == float("inf"):
        print("INF")
    else:
        print(weights[i + 1])
