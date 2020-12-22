def bintang(n):
    b = n//2
    a = n - b
    g = 1
    u = 1 + (b-1)*2
    s = 1 + b*2
    for i in range(a):
        n = "*" * g
        print(n.center(s))
        g +=2
    for i in range(b):
        m = "*" * u
        print(m.center(s))
        u -= 2
bintang(7)
