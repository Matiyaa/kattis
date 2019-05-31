from string import ascii_lowercase

alphabet = ascii_lowercase
n, m = map(int, input().split())
last_n = input()
cipher_text = input()
text = ''

for i in range(m - n):
    text += ' '

last_n = list(text + last_n)

for i in range(m - 1, n - 1, -1):
    last_n[i - n] = alphabet[(alphabet.index(cipher_text[i]) - alphabet.index(last_n[i]) % 26)]
last_n = ''.join(last_n)
print(last_n)
