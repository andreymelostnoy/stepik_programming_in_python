number_of_words = int(input())
words = []

for i in range(number_of_words):
    words.append(str(input()).lower())

number_of_lines = int(input())
lines = []

for i in range(number_of_lines):
    lines.append(str(input()).lower().split())

elements = []

for element in lines:
    for subelement in element:
        elements.append(subelement)

mistakes = []

for element in elements:
    if element not in words:
        if element not in mistakes:
            mistakes.append(element)

for mistake in mistakes:
    print(mistake)
