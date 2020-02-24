lst = [int(i) for i in input().split()]
x = int(input())

result = []
index_of_element = 0

for i in lst:
    if x == i:
        result.append(index_of_element)
    index_of_element += 1

if not result:
    print("Отсутствует")
else:
    print(*result)
