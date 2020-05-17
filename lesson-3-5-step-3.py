import sys

x = sys.argv
y = ""
for i in range(len(x)):
    if i == 0:
        pass
    else:
        y += x[i]
        y += " "

print(y.strip())
