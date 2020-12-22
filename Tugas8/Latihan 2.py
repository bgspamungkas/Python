def bintang(n):
    g = 1
    s = 1 + 2*(n)
    for i in range(n):
        b = "*" * g
        print(b.center(s))
        g +=2
bintang(5)
