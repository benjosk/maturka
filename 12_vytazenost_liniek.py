with open("12_bus_vytazenost.txt", "r", encoding="utf-8") as subor:
    fullka = int(subor.readline())
    f = subor.read().splitlines()

nad = []
pocet = 0
pocty = []
nazvy = []

for line in f:
    e = line.split(" ")
    nas, vys = int(e[0]), int(e[1])
    nazov = line[5:]
    nazvy.append(nazov)
    pocet += nas
    pocet -= vys
    if pocet > fullka:
        nad.append(nazov)
        pocty.append(pocet)


stanice = ", ".join(str(m) for m in nazvy)
plny = ", ".join(str(n) for n in nad)
pretazenie = max(pocty) - fullka

print(f"Maximálna kapacita autobusu je {fullka} miest.")
print(f"Počet staníc: {len(nazvy)}")
print(f"Zastávky na trase: {stanice}.")
print(f"Autobus bol preplnený na zastávkach: {plny}.")
print(f"Najväčšie preťaženie o {pretazenie} ľudí.")
