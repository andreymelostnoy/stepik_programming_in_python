n = int(input())
count = 0
result = 0
lst = []

while count != n:
    lst.append(int(input()))
    count += 1

for element in lst:
    result += element

print(result)
