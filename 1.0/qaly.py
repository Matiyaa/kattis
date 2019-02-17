x = int(input())
i = 0
life = 0
while i < x:
    q, y = map(float, input().split())
    life += q * y
    i += 1
print(life)
