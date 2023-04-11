// [문제 링크]: https://school.programmers.co.kr/learn/courses/30/lessons/154539?language=python3

def solution(numbers):
    answer = [-1] * len(numbers)
    stack = []
    for idx, n in enumerate(numbers):
        while stack and numbers[stack[-1]] < n:  # top이 가리키는 인덱스의 값보다 현재 값이 크면 현재 값이 top이 가리키는 곳의 뒤큰수
            tmp = stack.pop()
            answer[tmp] = n

        stack.append(idx)  # 스택에 현재 인덱스를 넣는다

    
    return answer