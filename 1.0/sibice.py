n, w, h = map(int, input().split())
maxlen = (w**2 + h**2)**0.5
for i in range(n):
    len_ = int(input())
    if len_ <= maxlen:
        print("DA")
    else:
        print("NE")
