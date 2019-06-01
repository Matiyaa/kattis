N, P, Q = map(int, input().split())
servers = ["paul", "opponent"]
score = P + Q
result = int((float(score) / N) % 2)
print(servers[result])
