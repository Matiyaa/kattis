N = int(input())
numbers = sum([i for i in list(map(int, input().split())) if i < 0])
print(numbers * -1)
