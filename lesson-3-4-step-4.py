import os


whole_text = ""

with open(os.path.join(".", "files", "dataset_3363_4.txt"),
          "r", encoding='utf-8') as file:
    with open(os.path.join(".", "files", "result.txt"), "w") as result_file:
        for line in file:
            whole_text += line
        pupils = whole_text.split(sep='\n')
        all_marks = []
        for i in pupils:
            marks = []
            for y in i.split(";"):
                if y.isdigit():
                    marks.append(int(y))
            all_marks.append(marks)
            x = sum(marks) / 3
            y = round(x, 9)
            result_file.write(str(y))
            result_file.write("\n")
        math_marks = []
        phys_marks = []
        russ_marks = []
        for i in all_marks:
            for y in range(len(i)):
                if y == 0:
                    math_marks.append(int(i[0]))
                elif y == 1:
                    phys_marks.append(int(i[1]))
                elif y == 2:
                    russ_marks.append(int(i[2]))
        average = ""
        av_math_marks = sum(math_marks) / len(math_marks)
        average += str(round(av_math_marks, 9))
        average += " "
        av_phys_marks = sum(phys_marks) / len(phys_marks)
        average += str(round(av_phys_marks, 9))
        average += " "
        av_russ_marks = sum(russ_marks) / len(russ_marks)
        average += str(round(av_russ_marks, 9))
        result_file.write(average)
