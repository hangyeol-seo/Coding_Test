def convert_base(n,k): #10진수 n을 k진수 문자열로 변환
    result=''
    while n>0:
        n,m=divmod(n,k)
        result+=str(m)
    return result[::-1]

def check_prime(n): #n이 소수인지 판단
    if n==1:
        return False
    m=int(n**(1/2))
    for i in range(2,m+1):
        if n%i==0:
            return False
    return True

def solution(n, k):
    answer = 0
    num=convert_base(n,k)
    len_num=len(num)
    zero_index=[-1]
    nums=[]
    
    for i in range(len_num):
        if num[i]=='0':
            zero_index.append(i)
            
    len_zero_index=len(zero_index)
    for i in range(1,len_zero_index):
        x=num[zero_index[i-1]+1:zero_index[i]]
        if x:
            nums.append(x)
        
    num=num[zero_index[-1]+1:]
    if num!='':
        nums.append(num)

    nums=list(map(int,nums))
    for num in nums:
        if check_prime(num):
            answer+=1

    return answer
