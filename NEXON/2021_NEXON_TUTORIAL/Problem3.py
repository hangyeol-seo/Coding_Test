def getMinimumMoves(arr):
    temp=sorted(arr)
    len_temp=len(temp)
    dic={}
    cnt=0
    for i in range(len_temp):
        dic[arr[i]]=i
    
    for i in range(1,len_temp):
        if dic[temp[i]]<dic[temp[i-1]]:
            cnt=len_temp-i
            break
    return cnt
    
