with open('note_stud.txt', 'rt') as f:
    linii=list(f)

n =media =0
print('Nume', 'Prenumele','Nota',sep='\t')
for linie in linii:
    campuri = linie.split()
    nota = int(campuri[2])
    n, media = n+1, media+nota

print(campuri[0],campuri[1],nota,sep='\t')
print("Media celor",n,"studenti este",media/float(n))