from itertools import combinations_with_replacement as comb

def cal_sum(temp,info):  
    score_lion=0
    score_apeach=0
    result=0
    for i in range(10,-1,-1):
        if temp[i]==0 and info[i]==0:
            continue
        if temp[i]>info[i]:
            score_lion+=(10-i)
        else:
            score_apeach+=(10-i)
    result=score_lion-score_apeach
    return result

def pick(c,result):
    for i in range(10,-1,-1):
        if c[i] > result[i]:
            return c
        elif c[i]<result[i]:
            return result
    return result
    
def solution(n, info):
    answer = []
    maximum=0
    result=[0,0,0,0,0,0,0,0,0,0,0]
    for c in comb([10,9,8,7,6,5,4,3,2,1,0],n):
        a=[0,0,0,0,0,0,0,0,0,0,0]
        for i in c:
            a[10-i]+=1
        s=cal_sum(a,info)
        if s>maximum:
            maximum=s
            result=a.copy()
        elif s==maximum:
            result=pick(a,result).copy()
    if maximum==0:
        answer=[-1]
    else:
        answer=result
    return answer
