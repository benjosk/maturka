import tkinter
def obrazok():
    jed = 0
    all = 0
    x,y = 0,0
    for i in range(len(f)):
        for znak in f[i].split():
            all += 1
            if znak == "1":
                jed += 1
                canvas.create_rectangle(x,y,x+1,y,fill="black",outline="black")
            else:
                canvas.create_rectangle(x,y,x+1,y,fill="white",outline="white")
            x += 1
        y += 1
        x = 0
    print(f"obrázok obsahuje {all} pixelov a {jed} je čiernych")
def preklopit():
    canvas.delete("all")
    x,y = int(velkost[0]),0
    for i in range(len(f)):
        for znak in f[i].split():
            if znak == "1":
                canvas.create_rectangle(x,y,x-1,y,fill="black",outline="black")
            else:
                canvas.create_rectangle(x,y,x-1,y,fill="white",outline="white")
            x -= 1
        y += 1
        x = int(velkost[0])
with open("preklopenie.txt", "r") as subor:
    velkost = subor.readline().split()
    f = subor.read().splitlines()
canvas = tkinter.Canvas(width=int(velkost[0]), height=int(velkost[1]))
canvas.pack()
b = tkinter.Button(text="preklopenie", command= preklopit)
b.pack()
obrazok()
canvas.mainloop()
