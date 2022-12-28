import sys
input = sys.stdin.readline

n = int(input())
string = input().strip()
visited = 0     # 몇 개 알파벳 사용중인지 체크
cnt = [0] * 26  # 해당 알파벳 사용 여부 확인

def add(x):
    global visited
    idx = ord(x) - ord('a')
    cnt[idx] += 1
    if cnt[idx] == 1:   # 새로 1이 되면 사용 갯수 추가
        visited += 1

def erase(x):
    global visited
    idx = ord(x) - ord('a')
    cnt[idx] -= 1
    if not cnt[idx]:    # 0이 되면 사용 갯수 감소
        visited -= 1

left = 0
ans = 0
for right in range(len(string)):  # 오른쪽 포인터가 먼저 가면서 왼쪽이 최대로 올 수 있는 곳 까지 확인
    add(string[right])            

    while visited > n:      # 오른쪽 이동은 종류 추가만 되기 때문에 왼쪽 한계까지 이동 가능
        erase(string[left])
        left += 1
    
    ans = max(ans, right - left + 1)  # left이상 right이하 string 길이

print(ans)

