N, Q = map(int, input().split())
locations = list(map(int, input().split()))
for i in range(Q):
    type_, data1, data2 = map(int, input().split())
    if type_ == 1:
        locations[data1 - 1] = data2
    elif type_ == 2:
        print(abs(locations[data2 - 1] - locations[data1 - 1]))
