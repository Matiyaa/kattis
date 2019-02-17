name = input()
n = len(name)
name_ = ''
for i in range(n):
    if i != n-1:
        if name[i] == name[i+1]:
            pass
        else:
            name_ += name[i]
    else:
        name_ += name[i]
print(name_)
