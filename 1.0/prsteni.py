N = int(input())
wheels = list(map(int, input().split()))
first_wheel = wheels[0]
wheels.remove(first_wheel)
for wheel in wheels:
    if first_wheel % wheel == 0:
        A = int(first_wheel / wheel)
        B = 1
        print(f'{A}/{B}')
    else:
        A = first_wheel
        B = wheel
        C = 1
        while C != 0:
            if A % 2 == 0 and B % 2 == 0:
                A = int(A / 2)
                B = int(B / 2)
            elif A % 3 == 0 and B % 3 == 0:
                A = int(A / 3)
                B = int(B / 3)
            elif A % 5 == 0 and B % 5 == 0:
                A = int(A / 5)
                B = int(B / 5)
            else:
                C = 0
        print(f'{A}/{B}')
