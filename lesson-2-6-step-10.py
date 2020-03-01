matrix = []

while True:
    users_input = input()
    if users_input == "end":
        break
    matrix.append(users_input.split())

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        elem = 0
        if (i == (len(matrix) - 1)) and (j == (len(matrix[i]) - 1)):
            elem = int(matrix[i - 1][j]) + int(matrix[0][j]) + int(matrix[i][j - 1]) + int(matrix[i][0])
        elif i == (len(matrix) - 1):
            elem = int(matrix[i - 1][j]) + int(matrix[0][j]) + int(matrix[i][j - 1]) + int(matrix[i][j + 1])
        elif j == (len(matrix[i]) - 1):
            elem = int(matrix[i - 1][j]) + int(matrix[i + 1][j]) + int(matrix[i][j - 1]) + int(matrix[i][0])
        else:
            elem = int(matrix[i - 1][j]) + int(matrix[i + 1][j]) + int(matrix[i][j - 1]) + int(matrix[i][j + 1])
        print(elem, end=' ')
    print()
