N = int(input())
word_count_A = 1
word_count_B = 0
for i in range(N):
    word_count_B += word_count_A
    word_count_A = word_count_B - word_count_A
print(f"{word_count_A} {word_count_B}")
