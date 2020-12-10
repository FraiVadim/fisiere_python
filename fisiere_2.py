f = open('note_stud.txt', 'r')
lst = list(f)
f.close()

for i in range (len(lst)):
    print( i+1, ':\t',lst[i])