stdin = input()
stdout = ""

length = len(stdin)
index_of_element_in_stdin = 0
max_elements = 0

# while index_of_element_in_stdin != length:
#     if length == 1:
#         stdout = stdin[index_of_element_in_stdin] + "1"
#     elif (index_of_element_in_stdin == length - 1) and (stdin[index_of_element_in_stdin] != stdin[-2]):
#         stdout = stdout + stdin[index_of_element_in_stdin] + "1"
#     elif stdin[index_of_element_in_stdin] == stdin[index_of_element_in_stdin + 1]:
#         max_elements += 1
#     elif (stdin[index_of_element_in_stdin] != stdin[index_of_element_in_stdin + 1]) and (
#             stdin[index_of_element_in_stdin] == stdin[index_of_element_in_stdin - 1]):
#         stdout = stdout + stdin[index_of_element_in_stdin] + str(max_elements)
#         max_elements = 0
#     else:
#         stdout = stdout + stdin[index_of_element_in_stdin] + "1"
#     index_of_element_in_stdin += 1
#
# # print(max_elements)
#
# # for i in range(length):
# #     if length == 1:
# #         stdout = stdin[i] + "1"
# #     elif (i == length - 1) and (stdin[i] != stdin[-2]):
# #         stdout = stdout + stdin[i] + "1"
# #     else:
# #         for j in i:
# #
# # for element in stdin:
# #     if length == 1:
# #         stdout = element + "1"
# #     elif (index_of_element_in_stdin == length - 1) and (element != stdin[-2]):
# #         stdout = stdout + element + "1"
# #     else:
#     #
#     # elif element == stdin[index_of_element_in_stdin + 1]:
#     #     max_elements += 1
#     # # else:
#     #     max_elements = 0
#     # index_of_element_in_stdin += 1
#

for element in stdin:
    if length == 1:
        max_elements += 1
    stdout = stdout + element + str(max_elements)
    index_of_element_in_stdin += 1

print(stdout)
