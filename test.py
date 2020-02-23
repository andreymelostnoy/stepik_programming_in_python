a = [int(i) for i in input().split()]
result = ""

if len(a) == 1:
    result = result + str(a[0])
else:
    iteration = 0
    for x in a:
        if iteration == (len(a) - 1):
            result = result + str((a[iteration - 1] + a[0]))
        else:
            result = result + str((a[iteration - 1] + a[iteration + 1])) + " "
        iteration += 1
print(result)
