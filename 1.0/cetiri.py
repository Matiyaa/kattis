numbers = [int(i) for i in input().split()]
numbers.sort()
x1 = numbers[1] - numbers[0]
x2 = numbers[2] - numbers[1]
if x1 == x2:
    print(numbers[2] + x1)
elif 2 * x1 == x2:
    print(numbers[1] + x1)
elif x1 == 2 * x2:
    print(numbers[0] + x2)
