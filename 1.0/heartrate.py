n = int(input())
for i in range(n):
    b, p = map(float, input().split())
    bpm = (60*b)/p
    minbpm = bpm - (60/p)
    maxbpm = bpm + (60/p)
    print(minbpm, bpm, maxbpm)
