import sys
input = sys.stdin.readline

n = input()
octa = int(n, 8)
print(bin(octa)[2:])
