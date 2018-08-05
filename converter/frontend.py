from tkinter import *
from tkinter import ttk

class Frontend:

    def __init__(self,master):
        #frame for the converter app
        self.holder=ttk.Frame(master,relief=SOLID,height=100,width=200,padding=(20,30))
        self.holder.pack()

        #input for temperature
        self.tempval=IntVar()
        self.temp=ttk.Entry(self.holder)
        self.temp.grid(row=0,column=0)


def main():
    root=Tk()
    root.geometry('680x500+50+50')
    #root.resizable(False,False)
    root.minsize(680,500)
    app=Frontend(root)
    root.mainloop()

main()