import tkinter

def kresli_graf(typgrafu, hodnoty=[], farba='lightgray'):
    suradnice = []
    nula = 250
    krok_x = 600 // 30
    krok_y = 250 // 40
    x = 40
    if typgrafu == 'pozadie':
        for i in range(nula, 400, krok_y*5):
            platno.create_line(x,i,600,i, fill=farba)
            platno.create_text(20, i, text=((-i+250)//krok_y))
        for i in range(nula, 0, -krok_y*5):
            platno.create_line(x,i,600,i, fill=farba)
            platno.create_text(20, i, text=((250 - i)//krok_y))
        platno.create_line(x, 0, x, 400)
        platno.create_line(0,nula,600,nula)
    else:
        for y in hodnoty:
            suradnice.append((x, nula - y * krok_y))
            x += krok_x
        if typgrafu == 'ciarovy':
            platno.create_line(suradnice, fill=farba)
        elif typgrafu == 'izolovane_body':
            for x,y in suradnice:
                r = 2
                platno.create_oval(x-r, y-r, x+r, y+r, fill=farba, outline='')
teploty = []
priemrene = []

with open("teploty.txt", "r") as subor:
    f = subor.read().splitlines()

for i in range(-1,(len(f)),4):
    priemrene.append(float(f[i]))

for i in range(len(f)):
    if float(f[i]) not in priemrene:
        teploty.append(int(f[i]))

priemS= ""
tepS = ""
vsetky = ""

for teplota in teploty:
    tepS += str(teplota) + ", "
for pr in priemrene[1:]:
    priemS += str(pr) + ", "
for t in f:
    vsetky += t + ", "


print("všetky teploty:", vsetky)
print("denné teploty:", tepS)
print("priemerne teploty:", priemS)
print("najvyššia priemrna teplota:", max(priemrene[1:]))


platno = tkinter.Canvas(width='600', height='400')
platno.pack()
kresli_graf('pozadie')
kresli_graf("ciarovy", teploty, "red")
kresli_graf("izolovane_body", teploty, "red")
kresli_graf("ciarovy", priemrene, "blue")
kresli_graf("izolovane_body", priemrene, "blue")
platno.mainloop()
