def solution(queue1, queue2):
    answer = 0
    sum_item = sum(queue1) + sum(queue2)
    queue3 = queue1 + queue2
    cur_sum = sum(queue1)
    
    if sum_item%2 != 0 :
        return -1

    target_value = sum_item // 2

    start = 0
    end = len(queue1)-1

    while target_value != cur_sum:
        if cur_sum > target_value:
            cur_sum -= queue3[start]
            start += 1
            answer += 1
            if start > end or start > len(queue3) : 
                return -1
        else:
            end += 1
            answer += 1
            if end == len(queue3):
                return -1 
            cur_sum += queue3[end]

    return answer

print(solution([1, 2, 1, 2], [1, 10, 1, 2]))