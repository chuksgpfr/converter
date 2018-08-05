from tkinter import *
from tkinter import ttk

class ConverterApp:

    def __init__(self,master):
        #Set The Window size
        master.geometry("400x400")

        #Window title
        master.title("Temperature Converter App")

        #Top title
        self.label=ttk.Label(master,text="Convert Temperature Easily")
        self.label.grid(row=0,column=0,columnspan=2)
        self.label.config(background='blue',justify=CENTER,foreground='white',font=('Courier',10,'bold'))
        self.logo=PhotoImage(file='temp.png');
        self.label.img=self.logo
        self.small_logo=self.label.img.subsample(2,2)
        self.label.config(image=self.small_logo,compound='left')

        self.temp=StringVar();
        self.cel=ttk.Radiobutton(master,variable=self.temp,text=u'\N{DEGREE SIGN}C',value='celsius')
        self.cel.grid(row=1,column=1)

        self.fah=ttk.Radiobutton(master,variable=self.temp,text=u'\N{DEGREE SIGN}F',value='fahreinheit')
        self.fah.grid(row=1,column=2)

        #Input for Temperature
        self.entry=ttk.Entry(master).grid(row=1,column=0)

        #Convert Button 

        self.convertBtn=ttk.Button(master,text="Convert").grid(row=1,column=3)




def main():
    root=Tk()
    app=ConverterApp(root)
    root.mainloop()

#if __name__ == "__main__":main()
main()