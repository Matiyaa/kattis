def solve_equation(_numbers_):
    symbols = []
    if _numbers_[0] + _numbers_[1] == _numbers_[2]:
        symbols = ['+', '=']
    elif _numbers_[0] - _numbers_[1] == _numbers_[2]:
        symbols = ['-', '=']
    elif _numbers_[0] / _numbers_[1] == _numbers_[2]:
        symbols = ['/', '=']
    elif _numbers_[0] * _numbers_[1] == _numbers_[2]:
        symbols = ['*', '=']
    elif not symbols:
        numbers_ = _numbers_[:]
        numbers_.append(_numbers_[0])
        numbers_.remove(_numbers_[0])
        equation = solve_equation(numbers_)
        a = len(str(_numbers_[1]))
        b = a + len(str(_numbers_[2])) + 1
        symbols = [equation[b], equation[a]]
    equation = f'{_numbers_[0]}{symbols[0]}{_numbers_[1]}{symbols[1]}{_numbers_[2]}'
    return equation


numbers = [int(i) for i in input().split()]
print(solve_equation(numbers))
