sum_M = 0
sum_S = 0
for i in range(int(input())):
    M, S = map(int, input().split())
    sum_M += M
    sum_S += S
minute = sum_S / (sum_M * 60)
if minute <= 1:
    print('measurement error')
else:
    print(minute)
