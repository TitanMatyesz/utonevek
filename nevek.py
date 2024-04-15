#osztaly
class Utonev:
    def __init__(self, nev, elso, masodik, uj1, uj2, nem):
        self.nev = nev
        self.elso = elso
        self.masodik = masodik
        self.uj1 = uj1
        self.uj2 = uj2
        self.nem = nem

    def __str__(self):
        return f"Utónév: {self.nev}, neme: {self.nem}"

#beolvasas
db = 0
utonevek = []
f = open("utonev.txt", "rt", encoding="ansi")
f.readline()

for sor in f:
    sor = sor.strip().split(';')
    print(sor)
    utonevek.append(Utonev(sor[0], sor[1], sor[2], sor[3], sor[4], sor[5]))
    db += 1

#adatok kiirasa
for utonev in utonevek:
    print(utonev)

#ferfiak szama
ffo = 0
for ferfi in utonevek:
    if ferfi.nem == 'F':
        if ferfi.elso != '':
            ffo += int(ferfi.elso)
print(f"{ffo} férfi volt")

#nok szama
nfo = 0
for no in utonevek:
    if no.nem == 'N':
        if no.elso != '':
            nfo += int(no.elso)
print(f"{nfo} nő volt")

print(f"{ffo + nfo} volt a népesség száma")
print(f"{db} utónévről van adat") 

#ujszuletett fiuk
ujfi = 0
for fiu in utonevek:
    if fiu.nem == 'F':
        if fiu.uj1 != '':
            ujfi += int(fiu.uj1)
ujfi2 = 0
for fiu2 in utonevek:
    if fiu2.nem == 'F':
        if fiu2.uj2 != '':
            ujfi2 += int(fiu.uj2)
print(f"{ujfi + ujfi2} újszülött fiú volt")