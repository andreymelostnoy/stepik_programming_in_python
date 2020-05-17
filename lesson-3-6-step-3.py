import requests

last_word = ""
file_name = "699991.txt"
count = 0

while last_word != "We":
    count += 1
    url = f"https://stepic.org/media/attachments/course67/3.6.3/{file_name}"

    r = requests.get(url.strip(), allow_redirects=True)
    out = open('text.txt', 'w')
    out.write(r.text)
    out.close()

    with open("text.txt", "r") as file:
        text = file.read()
        if "We" in text:
            last_word += "We"
        else:
            file_name = text

print(count)
