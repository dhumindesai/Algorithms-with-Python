def solution(A):
    n = len(A)

    total_sum = sum(A)
    current = 0
    previous = 0
    previous_sum = 0
    next_sum = 0

    for index, element in enumerate(A):
        previous_sum = previous_sum + previous
        total_sum = total_sum - element
        previous = element
        
        if previous_sum == total_sum:
            return index
    
    return -1

solution([-1,3,-4,5,1,-6,2,1])