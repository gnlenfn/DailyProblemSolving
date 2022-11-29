def solution(want, number, discount):
    left, right = 0, 9
    answer = 0
    
    target = [0] * len(want)
    tab = {name : idx for idx, name in enumerate(want)}

    for i in range(10):
        if discount[i] not in tab.keys():
            continue
        idx = tab[discount[i]]
        target[idx] += 1
    
    

    while right < len(discount) - 1:   
        left += 1
        right += 1

        if target == number:
            answer += 1    
        
        
        # move left point
        left_t = discount[left - 1]
        if left_t in want:
            left_t_idx = tab[left_t]
            target[left_t_idx] -= 1
        
        # move right point
        right_t = discount[right]
        if right_t in want:
            right_t_idx = tab[right_t]
            target[right_t_idx] += 1
        
    if target == number:
        answer += 1
        
        
    return answer