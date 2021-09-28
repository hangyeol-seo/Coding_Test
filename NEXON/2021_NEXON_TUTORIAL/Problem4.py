dx=[0,0,1,-1]
dy=[1,-1,0,0]

def dfs(start,visited,picture,len_picture0,len_picture):
    stack = list()
    stack.append(start)
    while stack:
        node = stack.pop()       
        visited[node[0]][node[1]]=1
        target = picture[node[0]][node[1]]
        for i in range(4):
            nx = node[0] + dx[i]
            ny = node[1] + dy[i]
            if 0 <= nx < len_picture and 0 <= ny < len_picture0:     
                if visited[nx][ny] == 0 and picture[nx][ny]==target:
                    stack.append((nx,ny))
                
def strokesRequired(picture):
    len_picture0=len(picture[0])
    len_picture=len(picture)
    visited=[[0 for _ in range(len_picture0)] for _ in range(len_picture)]
    cnt=0
    start=(0,0)
    while True:
        dfs(start,visited,picture,len_picture0,len_picture)
        cnt+=1
        check=0
        for i in range(len_picture):
            x=set(visited[i])
            if 0 in x:
                start=(i,visited[i].index(0))
                check=1
                break
        if check==0:
            break
    return cnt
