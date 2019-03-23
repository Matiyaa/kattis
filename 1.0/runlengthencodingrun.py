process, message = map(str, input().split())
processed_message = ''
if process == 'E':
    for i in message:
        if processed_message == '' or processed_message[-2] != i:
            processed_message += i + '1'
        else:
            count = int(processed_message[-1]) + 1
            processed_message = processed_message[:-1] + str(count)
elif process == 'D':
    length = int(len(message) / 2)
    for i in range(length):
        if i == 0:
            processed_message += message[i] * int(message[i + 1])
        else:
            processed_message += message[2 * i] * int(message[2 * i + 1])
print(processed_message)
