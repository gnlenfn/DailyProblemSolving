def solution(m, musicinfos):
    answer = []
    find_notes = transform(m)
    for idx, info in enumerate(musicinfos):
        start, end, title, codes = info.split(",")
        duration = get_duration(start, end)
        codes = transform(codes)

        if duration <= len(codes):
            played = codes[:duration]
        else:
            rep = duration // len(codes)
            played = codes * (rep + 1)
            played = played[:duration]
        
        if find_notes in played:
            answer.append((duration, idx, title))
    
    if answer:
        answer.sort(key=lambda x : (-x[0], x[1]))
        return answer[0][2]
    
    return "(None)"

def get_duration(start, end):
    start_h, start_m = map(int, start.split(":"))
    end_h, end_m = map(int, end.split(":"))
    
    # if end_h == 0 and end_m == 0:
    #     end_h = 24
    # 00:00 에 끝난 것을 24:00 으로 바꿔 처리한 경우 오히려 틀림 -> 이유 알 수 없음
    hours = end_h - start_h
    mins = 60 * hours + end_m - start_m
    return mins

def transform(codes):
    semi = {"C#": "c", "D#": "d", "F#": "f", "G#": "g", "A#": "a"}
    for key, val in semi.items():
        codes = codes.replace(key, val)

    return codes
    