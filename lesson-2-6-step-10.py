# НЕ РЕШЕНО
matrix = []

while True:
    users_input = input()
    if users_input == "end":
        break
    else:
        matrix.append(users_input.split())

new_matrix = []

for i in range(len(matrix)):
    print(type(i))
    for j in matrix[i]:
        print(j)

if len(new_matrix) == 1:
    pass

# print(matrix)
