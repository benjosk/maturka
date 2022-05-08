with open("Ftabulka_pocetnosti.txt", "r") as subor:
    f = subor.read().splitlines()
text = ""
for i in f:
    text += i
abeceda = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
nie = []
for pis in abeceda.lower():
    pocet = 0
    for znak in text.lower():
        if znak == pis:
            pocet += 1
    if pocet ==0:
        nie.append(pis.upper())
    print(f"{pis.upper()} - {pocet}")

print("písmena ktore nie su v texte:", nie)
