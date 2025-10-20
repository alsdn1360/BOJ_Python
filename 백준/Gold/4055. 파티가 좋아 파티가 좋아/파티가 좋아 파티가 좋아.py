# main
tc = 1

while True:
    p = int(input())

    if p == 0:
        break

    parties = sorted(list(tuple(map(int, input().split())) for _ in range(p)))
    attended_parties = [False] * p

    curr_time = 8

    while curr_time < 24:
        candidate_parties = []

        for i, (s, e) in enumerate(parties):
            if s <= curr_time < e and not attended_parties[i]:
                candidate_parties.append((e, i))  # 종료 시간, 그 파티의 인덱스

        candidate_parties.sort()  # 종료 시간이 가장 빠른 파티를 선택하기 위해 정렬

        if candidate_parties:
            attended_parties[candidate_parties[0][1]] = True  # 파티 참석 처리

        curr_time += 0.5

    attended_parties_cnt = attended_parties.count(True)

    print(f"On day {tc} Emma can attend as many as {attended_parties_cnt} parties.")

    tc += 1
