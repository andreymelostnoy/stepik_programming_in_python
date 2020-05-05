raw_lines = ""

with open("files/3-4-2", "r") as file:
    for line in file:
        raw_lines += line
        for element in line:
            pass


print(raw_lines)
