n = int(input())
for i in range(n):
    b, p = map(float, input().split())
    bpm = (60*b)/p
    min_bmp = bpm - (60 / p)
    max_bpm = bpm + (60 / p)
    print(min_bmp, bpm, max_bpm)
