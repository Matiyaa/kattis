arrivals = []
departures = []
timeline = {}
cost = 0
prices = list(map(int, input().split()))

for i in range(3):
    arrival, departure = map(int, input().split())
    arrivals.append(arrival)
    departures.append(departure)

for i in range(3):
    for j in range(arrivals[i], departures[i]):
        if j in timeline:
            timeline[j] += 1
        else:
            timeline[j] = 1

for i in timeline:
    if timeline[i] == 1:
        cost += prices[0]
    elif timeline[i] == 2:
        cost += prices[1] * 2
    elif timeline[i] == 3:
        cost += prices[2] * 3
print(cost)
