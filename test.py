a = [int(i) for i in input().split()]
a.sort()
pre_result = []
result = ""

for i in a:
    if (a.count(i) > 1) and i not in pre_result:
        a.remove(i)
        pre_result.append(i)

for element in pre_result:
        result = result + str(element) + " "

print(result)
