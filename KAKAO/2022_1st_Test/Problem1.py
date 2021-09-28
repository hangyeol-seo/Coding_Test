def solution(id_list, report, k):
    answer = []
    report_dic={} #유저별 신고한 ID저장
    reported_cnt={} #유저별 신고당한 횟수 저장
    reporting_cnt={} #유저가 신고해서 대상이 정지당한 횟수 저장
    
    for id in id_list:
        report_dic[id]=[]
        reported_cnt[id]=0
        reporting_cnt[id]=0
        
    for r in report:
        r=r.split()
        if r[1] not in report_dic[r[0]]:
            report_dic[r[0]].append(r[1])
            reported_cnt[r[1]]+=1
    
    for id in reported_cnt:
        if reported_cnt[id]>=k:
            for i in report_dic:
                if id in report_dic[i]:
                    reporting_cnt[i]+=1
    
    for id in id_list:
        answer.append(reporting_cnt[id])
        
    return answer
