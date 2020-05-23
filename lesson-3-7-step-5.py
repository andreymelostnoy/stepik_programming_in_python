import os


pupils = []
classes = {}
for i in range(11):
    classes[i + 1] = "-"

with open(os.path.join(".", "files", "tsv.txt"), "r", encoding="utf-8") as file:
    for line in file:
        pupils.append(line.strip().split("\t"))

for pupil in pupils:
    if classes[int(pupil[0])] == '-':
        classes[int(pupil[0])] = {}
    classes[int(pupil[0])][pupil[1]] = int(pupil[2])

for _class in classes:
    if classes[_class] == '-':
        print(_class, classes[_class])
    else:
        height = 0
        count = 0
        for i in classes[_class]:
            height += classes[_class][i]
            count += 1
        print(_class, height / count)


