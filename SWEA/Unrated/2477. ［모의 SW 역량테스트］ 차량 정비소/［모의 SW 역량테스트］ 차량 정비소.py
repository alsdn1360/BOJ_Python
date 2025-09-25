import heapq

# main
tc = int(input())

for test_case in range(1, tc + 1):
    # n: 접수 창구 개수
    # m: 정비 창구 개수
    # k: 고객의 수
    # a: 지갑을 두고 간 고객의 접수 창구번호
    # b: 지갑을 두고 간 고객의 정비 창구번호
    n, m, k, a, b = map(int, input().split())
    a_i = list(map(int, input().split()))  # i번째 접수 창구가 고장을 접수하는 데 걸리는 시간
    b_j = list(map(int, input().split()))  # j번째 정비 창구가 차량을 정비하는 데 걸리는 시간
    t_k = list(map(int, input().split()))  # k번째 고객이 차량 정비소를 방문하는 시간

    n_counter = [(0, 0)] * (n + 1)  # 접수 창구(끝나는 시간, 고객 번호)
    m_counter = [(0, 0, 0)] * (m + 1)  # 정비 창구(끝나는 시간, 고객 번호, 접수 창고 번호)

    n_queue = []  # 접수 창구 대기 큐 (고객번호 오름차순)
    m_queue = []  # 정비 창구 대기 큐 (접수 완료 오름차순, 접수 창구번호 오름차순, 고객 번호)

    time = 0
    customer_idx = 0

    end_customers = []  # (고객 번호, 접수 창고 번호, 정비 창고 번호)

    while len(end_customers) < k:
        # 1. 창구에서 업무가 끝난 고객 처리
        # 접수 창구 처리
        for i in range(1, n + 1):
            if n_counter[i] != (0, 0) and n_counter[i][0] == time:
                heapq.heappush(m_queue, (time, i, n_counter[i][1]))
                n_counter[i] = (0, 0)

        # 정비 창구 처리
        for j in range(1, m + 1):
            if m_counter[j] != (0, 0, 0) and m_counter[j][0] == time:
                end_customers.append((m_counter[j][1], m_counter[j][2], j))
                m_counter[j] = (0, 0, 0)

        # 2. 도착한 고객을 접수 창구 대기 큐에 추가
        while customer_idx < k:
            if t_k[customer_idx] == time:
                heapq.heappush(n_queue, customer_idx + 1)
                customer_idx += 1
            else:
                break

        # 3. 정비 창구 대기 큐에서 빈 정비 창구로 배정
        for j in range(1, m + 1):
            if m_counter[j] == (0, 0, 0) and m_queue:
                t, i, customer = heapq.heappop(m_queue)
                m_counter[j] = (time + b_j[j - 1], customer, i)

        # 4. 접수 창구 대기 큐에서 빈 접수 창구로 배정
        for i in range(1, n + 1):
            if n_counter[i] == (0, 0) and n_queue:
                customer = heapq.heappop(n_queue)
                n_counter[i] = (time + a_i[i - 1], customer)

        time += 1

    ans = 0

    for i in range(k):
        if end_customers[i][1] == a and end_customers[i][2] == b:
            ans += end_customers[i][0]

    print(f"#{test_case} {-1 if ans == 0 else ans}")
