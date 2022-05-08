import tkinter
def svetlo(n):
    canvas.create_rectangle(100,100,150,150, fill="black")
    canvas.create_rectangle(160,100,210,150, fill="black")
    canvas.create_rectangle(220,100,270,150, fill="black")
    if n < 25:
        canvas.create_oval(100, 100, 150, 150, fill="white")
        canvas.create_oval(160, 100, 210, 150, fill="white")
        canvas.create_oval(220, 100, 270, 150, fill="white")
    elif 25 <= n < 50:
        canvas.create_oval(100, 100, 150, 150, fill="white")
        canvas.create_oval(220, 100, 270, 150, fill="white")
    elif 50 <= n <= 70:
        canvas.create_oval(160, 100, 210, 150, fill="white")


canvas = tkinter.Canvas()
canvas.pack()

while True:
    try:
        n = int(input("intenzita osvetlenia v luxoch: "))
        break
    except ValueError:
        print("zlá hodnota")

svetlo(n)

canvas.mainloop()
