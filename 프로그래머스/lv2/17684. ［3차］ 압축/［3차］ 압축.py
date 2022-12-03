import string

def solution(msg):
    answer = []
    table = { let : idx for idx, let in enumerate(string.ascii_uppercase, 1)}
    
    idx = 0
    while idx < len(msg):
        if msg[idx] in table:
            d = 1
            while idx < len(msg):
                word = msg[idx: idx + d]

                if idx + d > len(msg):
                    if word in table:
                        answer.append(table[word])
                    
                    break

                if word in table:
                    d += 1
                    continue

                table[word] = len(table) + 1
                answer.append(table[word[:-1]])
                break

            idx += (d - 1)
    return answer
