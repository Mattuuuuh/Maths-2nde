def puissance(q, N):
    r = q
    for i in range(1, N+1):
        r = r * q
    return r

def fastexp(q, n):
    r = q
    for i in range(1,n+1):
        r = r*r
    return r
