import numpy as np

def countMoves(numbers):
    cnt=0
    if check_equal(numbers):
        return cnt
    else:
        len_numbers=len(numbers) 
        numbers=np.array(numbers)
        while True:
            maximum_index=np.where(numbers==max(numbers))
            numbers+=1
            numbers[maximum_index[0]]-=1
            cnt+=1
            if len(set(numbers))==1:
                break
    return cnt
