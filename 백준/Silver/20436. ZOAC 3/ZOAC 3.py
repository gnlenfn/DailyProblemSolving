left = {
    "q": (0, 0), "w": (0, 1), "e": (0, 2), "r": (0, 3), "t": (0, 4),
    "a": (1, 0), "s": (1, 1), "d": (1, 2), "f": (1, 3), "g": (1, 4),
    "z": (2, 0), "x": (2, 1), "c": (2, 2), "v": (2, 3)
}

right = {
    "y": (0, 5), "u": (0, 6), "i": (0, 7), "o": (0, 8), "p": (0, 9),
    "h": (1, 5), "j": (1, 6), "k": (1, 7), "l": (1, 8),
    "b": (2, 4), "n": (2, 5), "m": (2, 6)
}

l, r = input().split()
target_string = input()

ans = 0
for s in target_string:
    if s in left:
        cur = left[l]
        target = left[s]
        l = s

    else:
        cur = right[r]
        target = right[s]
        r = s

    ans += abs(cur[0] - target[0]) + abs(cur[1] - target[1])  # 이동 시간
    ans += 1  # 키 입력 시간

print(ans)
