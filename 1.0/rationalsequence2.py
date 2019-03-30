def function(left, right):
    n = 1
    path = ''
    if left == right:
        return n
    else:
        while left != 1 or right != 1:
            if left > right:
                path += 'R'
                left -= right
            elif right > left:
                path += 'L'
                right -= left
        path = path[::-1]
        for j in path:
            if j == 'L':
                n = n*2
            elif j == 'R':
                n = n*2 + 1
        return n


for i in range(int(input())):
    K, pq = input().split()
    p, q = map(int, pq.split('/'))
    print(K, function(p, q))
