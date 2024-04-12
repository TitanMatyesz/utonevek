class Utonevek:
    def __init__(self,utonev,elso,masodik,ujsz_1,ujsz_2,nem):
        self.utonev = utonev
        self.elso = elso
        self.masodik = masodik
        self.ujsz_1 = ujsz_1
        self.ujsz_2 = ujsz_2
        self.nem = nem
    
    def __str__(self):
        return f"Utónév: {self.utonev}, neme: {self.nem}"
    
f = open("utonev.txt", "rt", encoding="ANSI")
f.readline()

utonevek = []
for sor in f:
    tmp = sor.strip().split(";")
    utonevek.append(Utonevek(tmp[0],tmp[1],tmp[2],tmp[3],tmp[4],tmp[5]))

for nev in utonevek:
    print(nev)

'''
ferfi = 0
for nev in utonevek:
    if tmp[1] == "F":
        ferfi + 1
        print(ferfi)
        '''