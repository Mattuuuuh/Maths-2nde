def puissance(q, N):
    r = 1
    for i in range(N):
        r = r * q
    return r
def fastexp(q, n):
    r = q
    for i in range(n):
        r = r*r
    return r
