S1, S2, S3 = [0], [0], [0]
for i in range(1, 20002):
    S1.append(S1[-1]+i)
    if i % 2 != 0:
        S2.append(S2[-1]+i)
    else:
        S3.append(S3[-1]+i)
for i in range(int(input())):
    K, N = map(int, input().split())
    print(K, S1[N], S2[N], S3[N])
