import random, tkinter

canvas = tkinter.Canvas(height=400, width = 400)
canvas.pack()

styri = 0
pet = 0
for i in range(1000):
    cislo = random.randint(100, 999)
    if cislo % 5 == 0:
        pet += 1
    elif cislo % 4 == 0:
        styri += 1

canvas.create_line(30,30,30,370)
canvas.create_line(30,370,370,370)

canvas.create_rectangle(120,370,170,styri, fill= "red")
canvas.create_text(145,styri-10, text=styri)
canvas.create_text(145,380, text="delitelne 4")

canvas.create_rectangle(190,370,240,pet, fill= "blue")
canvas.create_text(215,pet-10, text=pet)
canvas.create_text(215,380, text="delitelne 5")
canvas.mainloop()
