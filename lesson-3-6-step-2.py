import requests

url = 'https://stepic.org/media/attachments/course67/3.6.2/580.txt'

r = requests.get(url.strip(), allow_redirects=True)
out = open('text.txt', 'w')
out.write(r.text)
out.close()

with open("text.txt", "r") as file:
    text = file.read()
    print(len(text.splitlines()))
