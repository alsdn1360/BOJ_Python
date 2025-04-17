from collections import Counter

def solution(weights):
    counts = Counter(weights)
    answer = 0

    # 1) 같은 무게끼리 (거리 2,3,4에서 짝 가능): c choose 2
    for w, c in counts.items():
        if c > 1:
            answer += c * (c - 1) // 2

    # 2) 다른 무게끼리 비율 검사 (거리 쌍 (2,3), (2,4), (3,4))
    for w, c in counts.items():
        # 거리 (2,3): w * 2 = p * 3  ⇒  p = 2w/3
        if (2*w) % 3 == 0:
            p = (2*w) // 3
            if p in counts and p < w:
                answer += c * counts[p]

        # 거리 (2,4): w * 2 = p * 4  ⇒  p = w/2
        if w % 2 == 0:
            p = w // 2
            if p in counts and p < w:
                answer += c * counts[p]

        # 거리 (3,4): w * 3 = p * 4  ⇒  p = 3w/4
        if (3*w) % 4 == 0:
            p = (3*w) // 4
            if p in counts and p < w:
                answer += c * counts[p]

    return answer
