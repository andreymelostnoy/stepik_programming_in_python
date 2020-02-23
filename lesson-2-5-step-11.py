a = [int(i) for i in input().split()]
a.sort()
print(a)
result = ""
index_count = 0

for i in range(len(a)):
    if len(a) <= 1:
        break
    elif i == a[-2]:
        if i == a[-1]:
            result = result + str(i) + " "
    elif i < len(a) - 2:
        if (a[index_count] == a[index_count + 1]) and (a[index_count + 1] != a[index_count + 2]):
            result = result + str(a[index_count]) + " "
    index_count += 1

print(result)
