def solution(id_list, report, k):
    answer = []
    
    user_report = {user : set() for user in id_list}
    user_reported_cnt = {user : 0 for user in id_list}
    
    for line in report:
        reporter, reported = line.split()
        
        if reported not in user_report[reporter]:
            user_report[reporter].add(reported)
            user_reported_cnt[reported] += 1
            
    suspension_user = {user for user, cnt in user_reported_cnt.items() if cnt >= k}
    
    for id in id_list:
        mail_cnt = len(user_report[id] & suspension_user)
        answer.append(mail_cnt)
        
    return answer