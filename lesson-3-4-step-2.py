import os


def genome_decoding(string):
    result = ""
    numbers = ""

    for i in range(len(string)):
        if i == 0:
            pass
        elif i == len(string) - 1:
            numbers += string[i]
            result += string[i - (len(numbers))] * int(numbers)
        elif string[i].isdigit():
            numbers += string[i]
        else:
            result += string[i - (len(numbers) + 1)] * int(numbers)
            numbers = ""

    return result


with open(os.path.join(".", "files", "dataset_3363_2.txt"), "r") as file:
    with open(os.path.join(".", "files", "result.txt"), "w") as result_file:
        for line in file:
            result_file.write(genome_decoding(line.strip()))
