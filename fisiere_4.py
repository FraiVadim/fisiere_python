with open('note_stud.txt', 'rt') as f:
    linii=f.readlines()

print(linii)
print()
for linie in  linii:
    print(linie.rstrip())