# test = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# n = 3
# a = [[0] * n] * n
# print(a)
#
# a[0][0] = 5
# print(a)
# print(len(a))
# print(a[0])
# print(a[1])
# print(a[2])
#
# a = [[0] * n for i in range(n)]
# print(a)
# a[0][0] = 5
# print(a)
#
# a = [[0 for j in range(n)] for i in range(n)]
# print(a)
# a[0][0] = 5
# print(a)
#
#
# sequence = [5, 8, 4, 3, 5, 7]
# m = sequence[0]
#
# for i in sequence:
#     if m > i:
#         m = i
#
# print(m)

# n, m, k = (int(i) for i in input().split())
# a = [[0 for j in range(m)] for i in range(n)]
#
# for i in range(k):
#     row, col = (int(i) -1 for i in input().split())
#     a[row][col] = -1
#
# for i in range(n):
#     for j in range(m):
#         if a [i][j] == 0:
#             for di in range(-1, 2):
#                 for dj in range(-1, 2):
#                     ai = i + di
#                     aj = j + dj
#                     if 0 <= ai < n and 0 <= aj < m and a[ai][aj] == -1:
#                         a[i][j] += 1
#
# for i in range(n):
#     for j in range(m):
#         if a[i][j] == -1:
#             print("*", end="")
#         elif a[i][j] == 0:
#             print(".", end="")
#         else:
#             print(a[i][j], end="")
#     print()
#
#
#
# kek = "1 2 2 3 3 3 4 4 4 4 5 5 5 5 5 6 6 6 6 6 6 7 7 7 7 7 7 7 8 8 8 8 8 8 8 8 9 9 9 9 9 9 9 9 9 10 10".split()
# print(kek)
# index_kek = 0
# for i in kek:
#     index_kek += 1
#
# print(index_kek)

