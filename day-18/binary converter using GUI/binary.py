from tkinter import*
from tkinter import messagebox
def binary():
    fn1=int(Fno.get())
    r=bin(fn1)
    messagebox.showinfo("output","result="+str(r))

def octal():
    fn1=int(Fno.get())
    r=oct(fn1)
    messagebox.showinfo("output","result="+str(r))
def hexadecimal():
    fn1=int(Fno.get())
    r=hex(fn1)
    messagebox.showinfo("output","result="+str(r))
###################
root=Tk()
root.title("MINI CONVERTER")
root.geometry("600x600")
Fno=StringVar()
Sno=StringVar()
#######################
binary = Button(root, text="BINARY",command=binary,width=15)
octal = Button(root, text="OCTAL",command=octal,width=15)
hexa = Button(root, text="HEXADECIMAL",command=hexadecimal,width=15)
cancel = Button(root,text="cancel",command=root.destroy,width=15)
#######################
Lb11 = Label(root,text="calculation")
fst_no = Label(root,text="enter a Number")

n1 = Entry(root,width=25,textvariable=Fno)
###########################
Lb11.grid(column=1,row=1,columnspan=2)
fst_no.grid(column=1,row=2)
n1.grid(column=2,row=2)
binary.grid(column=1,row=4)
octal.grid(column=2,row=4)
hexa.grid(column=1,row=5)
cancel.grid(column=2,row=5)
############################
root.mainloop()
