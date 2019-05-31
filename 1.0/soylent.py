for i in range(int(input())):
    intake = int(input())
    bottle = 400
    if int(intake / bottle) != intake / bottle:
        print(int(intake / bottle) + 1)
    else:
        print(int(intake / bottle))
