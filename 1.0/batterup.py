n = int(input())
list_ = list(map(int, input().split()))
n -= list_.count(-1)
sum_ = 0
for i in list_:
    if i != -1:
        sum_ += i
print(sum_/n)
