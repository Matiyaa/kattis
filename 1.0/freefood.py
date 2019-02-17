N = int(input())
days = []
for i in range(N):
    s, t = map(int, input().split())
    days_ = [j for j in range(s, t+1) if j not in days]
    days += set(days_)
print(len(days))
