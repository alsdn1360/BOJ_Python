from collections import deque

def solution(people, limit):
    n = len(people)
    answer = n
    
    people.sort(reverse=True)
    people = deque(people)
    
    while people:
        w = people.popleft()
        
        if people:
            remain_w = limit - w

            if remain_w >= people[-1]:
                people.pop()
                answer -= 1

    return answer
