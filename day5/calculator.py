from tkinter import *
from tkinter import messagebox

window=Tk()
window.title("CALCULATOR")
f=StringVar()
s=StringVar()

def calsum():
    fs=int(f.get())
    ss=int(s.get())
    r=fs+ss
    messagebox.showinfo("output","result="+str(r))
    messagebox.showinfo("confirmation page","done !!")
def calsub():
    fs=int(f.get())
    ss=int(s.get())
    r=fs-ss
    messagebox.showinfo("output","result="+str(r))
    messagebox.showinfo("done","result="+str(r))
    messagebox.showinfo("confirmation page","done !!")
def calmul():
    fs=int(f.get())
    ss=int(s.get())
    r=fs*ss
    messagebox.showinfo("output","result="+str(r))
    messagebox.showinfo("confirmation page","done !!")
def caldiv():
    fs=int(f.get())
    ss=int(s.get())
    r=fs/ss
    messagebox.showinfo("output","result="+str(r))
    messagebox.showinfo("confirmation page","done !!")
def calsqr():
    fs=int(f.get())
    ss=int(s.get())
    r=fs**(1/ss)
    messagebox.showinfo("output","result="+str(r))
    messagebox.showinfo("confirmation page","done !!")
def calsq():
    fs=int(f.get())
    ss=int(s.get())
    r=fs**ss
    messagebox.showinfo("output","result="+str(r))
    messagebox.showinfo("confirmation page","done !!")


add=Button(window, text='add', command=calsum, width=15)
add.grid(column=1, row=4)
sub=Button(window, text='subtract', command=calsub, width=15)
sub.grid(column=2, row=4)
mul=Button(window, text='multiply', command=calmul, width=15)
mul.grid(column=1, row=5)
div=Button(window, text='divide', command=caldiv, width=15)
div.grid(column=2, row=5)
sq=Button(window, text='square', command=calsq, width=15)
sq.grid(column=2, row=6)
sqr=Button(window, text='square root', command=calsqr, width=15)
sqr.grid(column=1, row=6)
cancel=Button(window, text='cancel', command=window.destroy, width=15)
cancel.grid(column=1,row=7,columnspan=2)

lb1=Label(window, text='Calculation')
lb1.grid(column=1, row=1, columnspan=2)
fs=Label(window, text='Enter the Number')
fs.grid(column=1,row=2)
ss=Label(window, text='Enter the Number')
ss.grid(column=1,row=3)
f=Entry(window, width=25, textvariable=f)
f.grid(column=2,row=2)
s=Entry(window, width=25, textvariable=s)
s.grid(column=2,row=3)


window.mainloop()
