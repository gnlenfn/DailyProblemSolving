import heapq

def solution(book_time):
    answer = 0
    
    # 분으로 변환
    book_min = []
    for start, end in book_time:
        start_h, start_m = map(int, start.split(":"))
        end_h, end_m = map(int, end.split(":"))
        book_min.append([start_h * 60 + start_m, end_h * 60 + end_m + 10])
        
    pq = []
    book_min.sort(key=lambda x: x[0])
    for start, end in book_min:
        while pq:
            if pq[0] <= start:
                heapq.heappop(pq)
            else:
                break
        
        heapq.heappush(pq, end)
        answer = max(answer, len(pq))
            
    return answer