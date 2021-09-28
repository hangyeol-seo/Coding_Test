import numpy as np

def solution(board, skill):
    answer = 0
    board=np.array(board)
    destroy=[]
    restore=[]
    destroy_append=destroy.append
    restore_append=restore.append
    
    for i in skill:
        if i[0]==1:
            destroy_append(i)
        else:
            restore_append(i)
    for i in destroy:
        x1=i[1]
        y1=i[2]
        x2=i[3]
        y2=i[4]
        degree=i[5]
        board[x1:x2+1,y1:y2+1]-=degree
    for i in restore:
        x1=i[1]
        y1=i[2]
        x2=i[3]
        y2=i[4]
        degree=i[5]
        board[x1:x2+1,y1:y2+1]+=degree
    
    answer=len(board[board>0])
    return answer
