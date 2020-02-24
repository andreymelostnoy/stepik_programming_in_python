stopper = 0
x = []
result = 0

while True:
    a = int(input())
    stopper = stopper + a
    x.append(a)
    if stopper == 0:
        for i in x:
            result = result + (i * i)
        break

print(result)
