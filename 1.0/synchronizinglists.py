while True:
    number = int(input())
    first_list = []
    second_list = []
    if number == 0:
        break
    else:
        for i in range(number):
            first_list.append(int(input()))
        for i in range(number):
            second_list.append(int(input()))
    sorted_first = sorted(first_list)
    sorted_second = sorted(second_list)
    for i in range(number):
        print(sorted_second[sorted_first.index(first_list[i])])
    print()
