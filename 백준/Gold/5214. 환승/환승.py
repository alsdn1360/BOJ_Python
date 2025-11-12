from collections import deque
import sys

input = sys.stdin.readline


def bfs():
    queue = deque([(1, 1)])
    visited_stations = {1}
    visited_tube = set()

    while queue:
        curr_station, cnt = queue.popleft()

        if curr_station == N:
            return cnt

        # 역이랑 연결되어있는 하이퍼튜브 탐색
        for tube_id in stations[curr_station]:
            if tube_id in visited_tube:
                continue

            # 하이퍼튜브 방문 처리
            visited_tube.add(tube_id)

            # 하이퍼튜브에 연결되어있는 역 탐색
            for adj_station in hyper_tubes[tube_id]:
                if adj_station in visited_stations:
                    continue

                # 역 방문 처리
                queue.append((adj_station, cnt + 1))
                visited_stations.add(adj_station)

    return -1


# main
N, K, M = map(int, input().split())

stations = {node: set() for node in range(1, N + 1)}  # 연결되어있는 하이퍼튜브의 번호
hyper_tubes = {node: [] for node in range(1, M + 1)}  # 하이퍼튜브가 연결하고 있는 역의 번호

for hyper_tube in range(1, M + 1):
    station_info = list(map(int, input().split()))

    for station in station_info:
        stations[station].add(hyper_tube)

    hyper_tubes[hyper_tube] = station_info

print(bfs())
