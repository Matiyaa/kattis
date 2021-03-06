def points_worth(number, suit, dominant):
    dominant_value = {"A": 11, "K": 4, "Q": 3, "J": 20, "T": 10, "9": 14, "8": 0, "7": 0}
    non_dominant_value = {"A": 11, "K": 4, "Q": 3, "J": 2, "T": 10, "9": 0, "8": 0, "7": 0}
    if suit == dominant:
        return dominant_value[number]
    else:
        return non_dominant_value[number]


a, b = input().split()
a = 4*int(a)
i = 0
sum_ = 0
while i < a:
    input_ = input()
    sum_ += points_worth(input_[0], input_[1], b)
    i += 1

print(sum_)
