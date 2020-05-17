import os


def max_counting_word(string):

    d = {}

    for i in sorted(string.lower().split()):
        d[i] = string.lower().split().count(i)

    max_value = max(d.values())
    max_dict = {k: v for k, v in d.items() if v == max_value}

    min_element = ""

    for i in min(max_dict.items()):
        min_element += str(i)
        min_element += " "

    return min_element.strip()


whole_text = ""

with open(os.path.join(".", "files", "dataset_3363_3.txt"), "r") as file:
    with open(os.path.join(".", "files", "result.txt"), "w") as result_file:
        for line in file:
            whole_text += line
        result_file.write(max_counting_word(whole_text))
