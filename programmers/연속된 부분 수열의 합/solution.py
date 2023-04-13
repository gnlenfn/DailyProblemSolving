// [문제 링크]: https://school.programmers.co.kr/learn/courses/30/lessons/178870

def solution(sequence, k):
    answer = []
    left, right = 0, 0
    s = sequence[0]
    while left <= right:
        if s == k:
            answer.append([left, right])

        if s <= k:
            right += 1
            if right >= len(sequence):
                break
            s += sequence[right]
        else:
            s -= sequence[left]
            left += 1
        

    answer = sorted(answer, key=lambda x: x[1] - x[0])
    return answer[0]
