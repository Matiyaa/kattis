N, M = map(int, input().split())
if N < M:
    if M - N == 1:
        print(f'Dr. Chaz will have {M - N} piece of chicken left over!')
    else:
        print(f'Dr. Chaz will have {M - N} pieces of chicken left over!')
else:
    if N - M == 1:
        print(f'Dr. Chaz needs {N - M} more piece of chicken!')
    else:
        print(f'Dr. Chaz needs {N - M} more pieces of chicken!')
