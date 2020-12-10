f = open('note_stud.txt', 'r')
lst = list(f)
f.close()

for i, linie in enumerate(lst):
    print( i+1, ':\t', linie, end='')