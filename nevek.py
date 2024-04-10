f = open("Utonev.txt", "rt", encoding="Ansi")

class Utonevek:
    def __init__(self,utonev,elso,masodik,ujsz_1,ujsz_2,nem):
        self.utonev = utonev
        self.elso = elso
        self.masodik = masodik
        self.ujsz_1 = ujsz_1
        self.ujsz_2 = ujsz_2
        nem = nem
    
    def __str__(self):
        return f"asdfsd"

nevek = []
for sor in f:
    tmp = sor.strip().split(";")
    nevek.append(Utonevek(tmp[0],tmp[1],tmp[2],tmp[3],tmp[4],tmp[5],))

for adat in nevek:
    print(adat)