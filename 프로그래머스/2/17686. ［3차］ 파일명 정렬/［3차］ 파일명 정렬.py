from collections import defaultdict
import re

def solution(files):
    answer = []
    folder = []
    
    for file in files:
        # 정규식을 이용해서 각각 분리
        # head: [^0-9] 숫자가 아닌 전부
        # number: [0-9]{1,5} 숫자인데, 0부터 99999사이
        # tail: 그 뒤 나머지
        head, number, tail = re.match('([^0-9]+)([0-9]{1,5})(.*)', file).groups()
        
        # 대소문자 상관없으므로 소문자로 처리
        folder.append((file, head.lower(), int(number)))
        
    # head 사전 기준으로 정렬하고 같으면, number 오름차순으로 정렬
    sorted_folder = sorted(folder, key = lambda x : (x[1], x[2]))
    
    # 파일명만 answer에 삽입
    answer = [x[0] for x in sorted_folder]
        
    return answer