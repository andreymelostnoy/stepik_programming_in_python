source_norm = str(input())
source_encr = str(input())
normal_text = str(input())
encrypted_text = str(input())

new_encrypted_text = ""
decoded_text = ""

for i in normal_text:
    if source_norm.find(i) == -1:
        new_encrypted_text += source_norm.find(i)
    else:
        new_encrypted_text += source_encr[source_norm.find(i)]

for i in encrypted_text:
    if source_encr.find(i) == -1:
        decoded_text += source_encr.find(i)
    else:
        decoded_text += source_norm[source_encr.find(i)]

print(new_encrypted_text)
print(decoded_text)
