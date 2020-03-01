# НЕ РЕШЕНО
# n = int(input())
n = 5
matrix = [[0] * n for i in range(n)]
offset = 0
current_number = 1
current_side = n

while offset < (current_side / 2):
    for i in range(current_side):
        matrix[offset][offset + i] = current_number
        current_number += 1
    for i in range(current_side - 2):
        matrix[1 + offset + i][n - 1 - offset] = current_number
        current_number += 1
    if (n / 2 - offset) > 0:
        for i in range(current_side):
            matrix[n - 1 - offset][n - 1 - i - offset] = current_number
            current_number += 1
    for i in range(current_side - 2):
        matrix[n - 2 - offset - i][offset] = current_number
        current_number += 1
    offset += 1
    current_side -= 2

for item in matrix:
    print(*item)
