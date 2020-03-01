genome = str(input())
result = ""
count = 0

for i in range(len(genome)):
    if i == (len(genome) - 1):
        if genome[i] == genome[i - 1]:
            count += 1
            result += (str(genome[i]) + str(count))
        else:
            count += 1
            result += (str(genome[i]) + str(count))
    else:
        if genome[i] == genome[i + 1]:
            count += 1
        else:
            count += 1
            result += (str(genome[i]) + str(count))
            count = 0

print(result)
