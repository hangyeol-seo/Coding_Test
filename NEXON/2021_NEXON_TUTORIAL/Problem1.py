def solve(X, arr, query_values):
    position=[]
    k=0
    for i in range(len(arr)):
        if arr[i]==X:
            position.append(i+1)
    
    for i in query_values:
        if i>len(position):
            print(-1)
        else:
            print(position[i-1])
    return
