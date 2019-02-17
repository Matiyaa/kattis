n = input()
done = False
while not done:
    sum_ = 0
    n = str(n)
    for i in n:
        sum_ += int(i)
    n = int(n)
    if n % sum_ == 0:
        print(n)
        done = True
    else:
        n += 1
