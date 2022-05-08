import tkinter,random

canvas = tkinter.Canvas(width=800,height=600)
canvas.pack()


def jablko(x,y,a):
    canvas.create_oval(x,y,x+a,y+a,fill="red")

def strom(x,y,vyska,jablka):
    canvas.create_line(x,600,x,y, width=vyska/2, fill="brown")
    canvas.create_oval(x-vyska,y-vyska,x+vyska,y+vyska,fill="green")
    for i in range(jablka):
        jablko(random.randint(x-vyska,x+vyska),random.randint(y-vyska,y+vyska),vyska/4)

for i in range(3):
    strom(random.randint(50,750),random.randint(50,550),random.randint(20,100),2)
canvas.mainloop()
