text = input()
vowels = ['a', 'e', 'i', 'o', 'u']
output = ""
working = True
i = 0
while i < len(text):
    if text[i] in vowels:
        output += text[i]
        i += 3
    else:
        output += text[i]
        i += 1
print(output)
