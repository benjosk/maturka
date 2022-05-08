import tkinter, random

def mozaika(stvorec,subor):
    x,y = 0,0
    subor.write(str(stvorec)+"\n")
    for j in range(int(400/stvorec + stvorec)):
        for i in range(int(600/stvorec + stvorec)):
            farba = f"#{random.randrange(256):02x}{random.randrange(256):02x}{random.randrange(256):02x}"
            canvas.create_rectangle(x,y,x+stvorec,y+stvorec, fill= farba, outline= farba)
            subor.write(farba+"\n")
            x+=stvorec
        x = 0
        y+=stvorec

canvas = tkinter.Canvas(height = 400, width= 600)
canvas.pack()

subor = open("10_mozaika.txt", "w")
mozaika(random.randrange(5,30),subor)
subor.close()
canvas.mainloop()
