import turtle,random
def hodina(f1,f2):
    t.down()
    t.color(f1)
    t.width(10)
    t.fillcolor(f2)
    t.begin_fill()
    t.forward(100)
    t.setheading(-120)
    t.forward(200)
    t.setheading(0)
    t.forward(100)
    t.setheading(120)
    t.forward(200)
    t.setheading(0)
    t.forward(100)
    t.end_fill()
t = turtle.Turtle()
t.speed(0)
t.up()
t.setpos(-280,200)
canvas = turtle.Screen()
farby = ["red", "blue", "green", "pink", "yellow"]
f1 = random.choice(farby)
farby.remove(f1)
f2 = random.choice(farby)
for i in range(5):
    hodina(f1,f2)
    f1,f2 = f2,f1
canvas.mainloop()
