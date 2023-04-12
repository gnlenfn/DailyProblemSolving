from bisect import bisect_left

n = int(input())
nums = list(map(int, input().split()))
m = int(input())
targets = list(map(int, input().split()))

nums.sort()

answer = []
for num in targets:  # 확인 할 숫자들을 순회
    idx = bisect_left(nums, num)  # 상근이가 가진 카드들을 이분 탐색
    if idx == n:
        answer.append('0')  # 맨 뒤에 insert, 하지만 없는 카드라 추가되어야 하고 index out of range

    elif nums[idx] == num:  # bisect_left는 num이 들어갈 위치의 왼쪽 인덱스를 반환 -> num과 그 왼쪽인덱스의 값이 같으면 가지고있는 카드
        answer.append('1')
    else:
        answer.append('0')  # join 시 타입 에러 때문에 string으로 append

print(" ".join(answer))