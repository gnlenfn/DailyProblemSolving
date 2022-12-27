import sys

n = int(sys.stdin.readline().strip())
lq = list(map(int, sys.stdin.readline().split()))

lq.sort()  # O(nlogn)

left, right = 0, len(lq) - 1

current = float("inf")
while left < right:
    if abs(lq[left] + lq[right]) < current:  # 혼합 특성값이 기존보다 0에 가까움!
        current = abs(lq[left] + lq[right])
        ans = [lq[left], lq[right]]

    if lq[left] + lq[right] < 0: # 특성값이 음수면 왼쪽이동 (더 크게 만들어)
        left += 1
    else:
        right -= 1  # 특성값이 양수면 오른쪽 이동 (더 작게 만들어)
    

ans.sort()
print(ans[0], ans[1])