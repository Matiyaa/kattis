D, M = map(int, input().split())
days = ["Thursday", "Friday", "Saturday", "Sunday", "Monday", "Tuesday", "Wednesday"]
months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
D += sum(months[0:(M-1)])
D = (D % 7) - 1
print(days[D])
