A, B, C = map(int, input().split())
I, J, K = map(int, input().split())
min_ = min(A/I, B/J, C/K)
print(A-(I*min_), B-(J*min_), C-(K*min_))
