from tkinter import *

class Paint(object):
    def __init__(self):
        self.window = Tk()
        self.window.title("Colour paint")
        self.window.geometry("600x600")
        self.window.configure(background=("light grey"))

        self.penbutton = Button(self.window,text="pen",width=10)
        self.penbutton.grid(row=1,column=0)

        self.brushbutton = Button(self.window,text="brush",width=10)
        self.brushbutton.grid(row=1,column=1)

        self.colorbutton = Button(self.window,text="color",width=10)
        self.colorbutton.grid(row=1,column=2)

        self.eraserbutton = Button(self.window,text="eraser",width=10)
        self.eraserbutton.grid(row=1,column=3)

        self.scale = Scale(self.window,from_=1,to=5,orient=HORIZONTAL)
        self.scale.grid(row=1,column=4)
        self.canvas = Canvas(self.window,bg="white",width=605,height=575)
        self.canvas.grid(row=2,columnspan=5)
        self.window.mainloop()
Paint()
