def sieve(n):
	is_prime = [True] * (n+1)
	is_prime[0] = False
	is_prime[1] = False

	for candidate in range(2, n+1):
		if not is_prime[candidate]:
			continue
		for multiple in range(candidate*candidate, n+1, candidate):
			is_prime[multiple] = False

	return [idx for idx, value in enumerate(is_prime) if value]

def sol():
    n = int(input())
    if n == 1:
        return 0

    p = sieve(n)
    psum = p[0]
    l = r = 0
    cnt = 0
    while l <= r and r < len(p):
        if psum < n:
            r += 1
            if r >= len(p):
                break
            psum += p[r]
        
        elif psum > n:
            psum -= p[l]
            l += 1
        
        if psum == n:
            cnt += 1
            r += 1
            if r >= len(p):
                break
            psum += p[r]

    return cnt

print(sol())

