import random
subor = open("09_studenti.txt", "r", encoding="utf-8")
f = subor.read().splitlines()
f.sort()
subor.close()
dievcata = []
chalpci = []
for meno in f:
    if "ová" in meno or "ova" in meno or "ská" in meno or "cká" in meno:
        dievcata.append(meno)
    elif meno == 'Krajňak Alica':
        dievcata.append(meno)
    else:
        chalpci.append(meno)
strCH =""
for meno in chalpci:
    strCH += meno + ", "
strD = ""
for meno in dievcata:
    strD += meno + ", "
print("pocet dievcat: ", len(dievcata))
print(strD)
print("pocet chlapcov: ", len(chalpci))
print(strCH)
print(f"zodpovední za porgram sú {random.choice(dievcata)} a {random.choice(chalpci)}")
