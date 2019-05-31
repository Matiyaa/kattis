n, w, h = map(int, input().split())
max_len = (w ** 2 + h ** 2) ** 0.5
for i in range(n):
    len_ = int(input())
    if len_ <= max_len:
        print("DA")
    else:
        print("NE")
