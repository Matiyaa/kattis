C = float(input())
L = int(input())
cost = 0
for i in range(L):
    w, l = map(float, input().split())
    area = w * l
    cost += C * area
print(cost)
