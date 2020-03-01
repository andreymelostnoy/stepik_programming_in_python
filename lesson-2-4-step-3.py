genome = str(input()).lower()

gc = 0
for i in genome:
    if (i in 'g') or (i in 'c'):
        gc += 1

print(gc / len(genome) * 100)
