number1 = bin(int(input()))
number2 = '0b' + number1[:1:-1]
number2 = int(number2, 2)
print(number2)
