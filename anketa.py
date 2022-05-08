import tkinter
canvas = tkinter.Canvas(width = 500, height=300, bg="grey")
canvas.pack()

with open("anketa.txt", "r", encoding="utf-8") as subor:
    otazka = subor.readline()
    odpovede = subor.read().split()

def klik(eff=None, odp=odpovede, otaz=otazka):
    with open("anketa.txt", "w", encoding="utf-8") as subor:
        subor.write(otaz + "\n")
        subor.write(f"{int(odp[0])+1} {odp[1]} {odp[2]}")
    global farba1
    canvas.create_rectangle(120, 90, 120 + int(odpovede[0])+1, 110, fill=farba1)
    canvas.create_rectangle(60,90,76,110,fill="grey",outline="grey")
    canvas.create_text(66, 100, text=f"{int(odpovede[0])+1}")


def klik2(eff=None, odp=odpovede, otaz=otazka):
    with open("anketa.txt", "w", encoding="utf-8") as subor:
        subor.write(otaz + "\n")
        subor.write(f"{odp[0]} {int(odp[1])+1} {odp[2]}")
    global farba2
    canvas.create_rectangle(120, 130, 120 + int(odpovede[1])+1, 150, fill=farba2)
    canvas.create_rectangle(58,130,76,150,fill="grey",outline="grey")
    canvas.create_text(64, 140, text=f"{int(odpovede[1])+1}")


def klik3(eff=None, odp=odpovede, otaz=otazka):
    with open("anketa.txt", "w", encoding="utf-8") as subor:
        subor.write(otaz + "\n")
        subor.write(f"{odp[0]} {odp[1]} {int(odp[2])+1}")
    global farba3
    canvas.create_rectangle(120, 170, 120 + int(odpovede[2])+1, 190, fill=farba3)
    canvas.create_rectangle(70,170,80,190,fill="grey",outline="grey")
    canvas.create_text(75, 180, text=f"{int(odpovede[2])+1}")

cislaOD= []
for c in odpovede:
    cislaOD.append(int(c))
farba = ["0", "1", "2"]
farba1 = "red"
farba2 = "red"
farba3 = "red"

ind = cislaOD.index(max(cislaOD))
if str(ind) == farba[0]:
    farba1 = "green"
elif str(ind) == farba[1]:
    farba2 = "green"
elif str(ind) == farba[2]:
    farba3 = "green"


canvas.create_text(250, 50, text=otazka)

canvas.create_text(15, 100, text="1)", tags="cislo")
canvas.create_text(50, 100, text=f"áno - {odpovede[0]}")

canvas.create_text(15, 140, text="2)", tags="cislo2")
canvas.create_text(50, 140, text=f"nie - {odpovede[1]}")

canvas.create_text(15, 180, text="3)", tags="cislo3")
canvas.create_text(50, 180, text=f"neviem - {odpovede[2]}")

canvas.create_rectangle(120,90,120+int(odpovede[0]), 110, fill=farba1)
canvas.create_rectangle(120,130,120+int(odpovede[1]), 150, fill=farba2)
canvas.create_rectangle(120,170,120+int(odpovede[2]), 190, fill=farba3)

canvas.tag_bind("cislo", "<Button-1>",lambda eff: klik(eff, odp=odpovede, otaz=otazka) )
canvas.tag_bind("cislo2", "<Button-1>",lambda eff: klik2(eff, odp=odpovede, otaz=otazka) )
canvas.tag_bind("cislo3", "<Button-1>",lambda eff: klik3(eff, odp=odpovede, otaz=otazka) )

canvas.mainloop()
