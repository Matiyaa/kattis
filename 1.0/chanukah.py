candles = [2]
for i in range(2, 10001):
    candles.append(candles[-1]+i+1)
for i in range(int(input())):
    K, N = map(int, input().split())
    print(K, candles[N-1])
