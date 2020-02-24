x = int(input())
sequance = []
result = []
q = []

for element in range(1, x + 1):
    sequance.append(element)

for element in sequance:
    result.append([element] * element)

for i in range(x):
    for j in result[i]:
        q.append(j)

print(*q[:x])
