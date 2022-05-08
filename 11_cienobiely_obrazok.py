import tkinter
def obrazok(zvacsenie):
    global sirka,vyska
    sirka, vyska = sirka*zvacsenie, vyska*zvacsenie
    canvas.config(width=sirka,height=vyska)
    x, y = 0, 0
    p = 1
    for riadok in pixely:
        for i in range(int(len(riadok)/2)):
            pixel = str(riadok[p-1]) + str(riadok[p])
            farba = f"#{pixel}{pixel}{pixel}"
            canvas.create_rectangle(x,y,x+1*zvacsenie,y,fill=farba, outline=farba)
            x += 1*zvacsenie
            p += 2
        y += 1*zvacsenie
        x,p = 0,1
with open("11_sen.txt", "r") as subor:
    rozmery = subor.readline().split()
    pixely = subor.read().splitlines()
sirka, vyska = int(rozmery[0]), int(rozmery[1])
canvas = tkinter.Canvas(width=sirka, height=vyska)
canvas.pack()
while True:
    try:
        n = int(input("zadaj číslo zväčšenia z intervalu <1,4> : "))
        if 1 <= n <= 4:
            break
        else:
            raise ValueError
    except ValueError:
        print("zlá hodnota")
obrazok(n)
canvas.mainloop()
