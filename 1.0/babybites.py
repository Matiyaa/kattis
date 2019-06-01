N = int(input())
counting = input().split()
count = 1
for word in counting:
    if word == 'mumble':
        count += 1
    else:
        if int(word) == count:
            count += 1
        else:
            print('something is fishy')
            exit()
print('makes sense')
