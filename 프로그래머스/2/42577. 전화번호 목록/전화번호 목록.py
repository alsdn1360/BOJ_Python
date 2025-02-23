def solution(phone_book):
    # 전화번호 목록 사전순으로 정렬
    phone_book.sort()
    
    # 현재 전화번호와 바로 다음 전화번호 비교
    for i in range(len(phone_book) - 1):
        # 접두사를 찾기 위한 startwith()
        if phone_book[i + 1].startswith(phone_book[i]):
            return False
        
    return True
