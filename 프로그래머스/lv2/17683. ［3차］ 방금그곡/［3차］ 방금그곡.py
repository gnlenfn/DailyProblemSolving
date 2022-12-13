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
    
    hours = abs(end_h - start_h)
    mins = 60 * hours + end_m - start_m
    return mins

def transform(codes):
    while codes.find("#") > 0:
        idx = codes.index("#")
        codes = codes[:idx-1] + codes[idx-1].lower() + codes[idx+1:]
        
    return codes
    