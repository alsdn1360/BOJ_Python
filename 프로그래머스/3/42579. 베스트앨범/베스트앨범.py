def solution(genres, plays):
    answer = []
    
    # 앨범과 장르 별 전체 재생 수를 위한 딕셔너리 생성
    album = {genre : [] for genre in set(genres)}
    total_plays = {genre : 0 for genre in set(genres)} 
    
    # 장르 별로 고유번호와 재생 수를 앨범에 넣고, 전체 재생 수를 구함
    for i in range(len(plays)):
        album[genres[i]].append((i, plays[i]))
        total_plays[genres[i]] += plays[i]
        
    # 내림차순으로 전체 재생 수 정렬
    total_plays = sorted(total_plays.items(), key = lambda x : x[1], reverse = True)
    
    # 현재 전체 재생수는 (장르, 전체 재생 수)로 되어있기 때문에 genre, _는 장르만 이용하겠다는 뜻
    for genre, _ in total_plays:
        # 앨범에서 장르 별로 재생 수는 내림차순, 고유번호는 오름차순으로 정렬
        # x[1]는 재생 수, -x[0]은 고유번호(reverse = True이기 때문에 앞에 - 붙임)
        sorted_album = sorted(album[genre], key = lambda x : (x[1], -x[0]), reverse = True)
        
        # i for i, _ 는 재생 수는 이용하지 않고 i만 쓰겠다는 뜻
        answer.extend([i for i, _ in sorted_album[:2]])
        
    return answer